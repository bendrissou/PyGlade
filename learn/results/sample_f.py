# ### Fuzzer

import random
import pprint
import copy
# +
class Fuzzer:
    def __init__(self, grammar):
        self.grammar = grammar

    def fuzz(self, key='<start>', max_num=None, max_depth=None):
        raise NotImplemented()

COST = None

# CheckFuzzer class implements the check construction for merges
# For each merge, two checks are constructed, follwoing section 5.3.
# The new key recently added into a grammar is assigned a cost of -1,
# ie: the least cost, that is to insure that it gets expanded first.
class CheckFuzzer(Fuzzer):
    def symbol_cost(self, grammar, symbol, seen):
        if symbol in self.key_cost: return self.key_cost[symbol]
        if symbol in seen:
            self.key_cost[symbol] = float('inf')
            return float('inf')
        if symbol == self.key:
            v = -1
        else:
            v = min((self.expansion_cost(grammar, rule, seen | {symbol})
                        for rule in grammar.get(symbol, [])), default=0)
        self.key_cost[symbol] = v
        return v

    def expansion_cost(self, grammar, tokens, seen):
        if min((self.symbol_cost(grammar, token, seen) for token in tokens if token in grammar), default=0) == -1:
            return -1
        else:
            return max((self.symbol_cost(grammar, token, seen)
                        for token in tokens if token in grammar), default=0) + 1

    def gen_key(self, key, depth, max_depth):
        if key not in self.grammar: return key

        elif key == self.key:
            if self.check == 2:
                # 2 repetitions have been generated. Stop there.
                rules = [self.grammar[key][1]]
            else:
                rules = [self.grammar[key][0]]
                self.check += 1

        else:
            pathl = [(key, rule) for rule in self.grammar[key] if self.cost[key][str(rule)] == -1]
            if len(pathl) > 1:
                clst = sorted([(self.normal_cost[k][str(r)], r) for k, r in pathl])
            else:
                clst = sorted([(self.cost[key][str(rule)], rule) for rule in self.grammar[key]])
            rules = [r for c,r in clst if c == clst[0][0]]

        chosen_rule = random.choice(rules)
        current_expansion = key + ''.join(chosen_rule)
        if key.endswith('_rep>') and key != self.key and current_expansion in self.past_expansions: 
            if clst[0][0] == -1 and len(clst) > 1:
                # Take the second cheapest path to avoid potential infinite loops.
                rules = [r for c,r in clst if c == clst[1][0]]
                chosen_rule = random.choice(rules)
  
        # The following to ensure that the traget non-terminal rule is set back to the original rule with rep of 1.
        chosen_rule = [self.ini_token if key != self.key and token == self.key and self.check == 2 else token for token in chosen_rule]
        current_expansion = key + ''.join(chosen_rule)
 
        self.past_expansions.add(current_expansion)
        return self.gen_rule(chosen_rule, depth+1, max_depth)

    def gen_rule(self, rule, depth, max_depth):
        return ''.join(self.gen_key(token, depth, max_depth) for token in rule)

    def fuzz(self, key='<start>', max_depth=100):
        self.past_expansions = set()
        return self.gen_key(key=key, depth=0, max_depth=max_depth)

    def reduce_reps(self, grammar):
        # Set all repetitions to 1 repetition. Except for the traget non-terminal.
        new_g = copy.deepcopy(grammar)
        for k in new_g:
            if k.endswith('rep>') and k != self.key:
                new_g[k] = [[new_g[k][0][1]]]
        return new_g

    def __init__(self, grammar, key, ini_token):
        global COST
        self.key = key
        self.ini_token = ini_token
        ng = self.reduce_reps(grammar)
        super().__init__(ng)
        self.check = 0
        self.past_expansions = set()
        self.alt = 0 # First alternative index to try.
        self.key_cost = {}
        COST = self.compute_cost(ng)
        self.cost = COST
        self.normal_cost = LimitFuzzer(ng).cost

    def compute_cost(self, grammar):
        cost = {}
        for k in grammar:
            cost[k] = {}
            for rule in grammar[k]:
                try:
                    cost[k][str(rule)] = self.expansion_cost(grammar, rule, set())
                except Exception as e:
                    cost[k][str(rule)] = float('inf')
        return cost

class LimitFuzzer(Fuzzer):
    def symbol_cost(self, grammar, symbol, seen):
        if symbol in self.key_cost: return self.key_cost[symbol]
        if symbol in seen:
            self.key_cost[symbol] = float('inf')
            return float('inf')
        v = min((self.expansion_cost(grammar, rule, seen | {symbol})
                    for rule in grammar.get(symbol, [])), default=0)
        self.key_cost[symbol] = v
        return v

    def expansion_cost(self, grammar, tokens, seen):
        return max((self.symbol_cost(grammar, token, seen)
                    for token in tokens if token in grammar), default=0) + 1

    def gen_key(self, key, depth, max_depth):
        if key not in self.grammar: return key
        if depth > max_depth:
            clst = sorted([(self.cost[key][str(rule)], rule) for rule in self.grammar[key]])
            rules = [r for c,r in clst if c == clst[0][0]]
        else:
            print("Key: " + key)
            rules = self.grammar[key]
        return self.gen_rule(random.choice(rules), depth+1, max_depth)

    def gen_rule(self, rule, depth, max_depth):
        return ''.join(self.gen_key(token, depth, max_depth) for token in rule)

    def fuzz(self, key='<start>', max_depth=100):
        return self.gen_key(key=key, depth=0, max_depth=max_depth)

    def __init__(self, grammar):
        global counter
        super().__init__(grammar)
        self.key_cost = {}
        COST = self.compute_cost(grammar)
        self.cost = COST

    def compute_cost(self, grammar):
        cost = {}
        for k in grammar:
            cost[k] = {}
            for rule in grammar[k]:
                try:
                    cost[k][str(rule)] = self.expansion_cost(grammar, rule, set())
                except Exception as e:
                    cost[k][str(rule)] = float('inf')
        return cost

import json

def sample(fn, ty):
    #open('../../seeds/%s_inputs.txt' % fn, 'w').close()   # erase file content
    with open("../" + ty + "/" + fn + ".json") as f: # synthesized  handwritten
        mgrammar = json.load(fp=f)
    fuzzer = LimitFuzzer(mgrammar)
    correct = 0
    total = 1000
    #b = open('../../seeds/%s_inputs.txt' % fn, "w")
    #for i in range(total):
    i = 0
    while True:
        if i == total: break

        val = fuzzer.fuzz(mgrammar['<start>'][0][0])

        if len(val) > 200 or len(val) == 0: continue
        i += 1

        if ty == 'handwritten': val = val + '\n'
        new_file = '../samples/' + ty + '/' + fn + '/input_' + str(i) + '.in'
        fout = open(new_file, "wt")
        fout.write(val)
        fout.close()
    print("Finished sampling.")

if __name__ == '__main__':
    import sys
    antlr_programs = ['xpath', 'lua', 'pascal', 'mysql', 'c', 'tinyc', 'tiny', 'basic']
    program = sys.argv[1]
    if program not in antlr_programs: sample(program, 'handwritten')
    sample(program, 'synthesized')
