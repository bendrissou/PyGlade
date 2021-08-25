grammar = {
    '<start>': [['<expr>']],
    '<expr>': [
        ['<term>', '+', '<expr>'],
        ['<term>', '-', '<expr>'],
        ['<term>']],
    '<term>': [
        ['<fact>', '*', '<term>'],
        ['<fact>', '/', '<term>'],
        ['<fact>']],
    '<fact>': [
        ['<digits>'],
        ['(','<expr>',')']],
    '<digits>': [
        ['<digit>','<digits>'],
        ['<digit>']],
    '<digit>': [["%s" % str(i)] for i in range(10)],
}
START = '<start>'

# Here is another grammar that targets the same language. Unlike the first
# grammar, this grammar produces ambiguous parse results.

a_grammar = {
    '<start>': [['<expr>']],
    '<expr>': [
        ['<expr>', '+', '<expr>'],
        ['<expr>', '-', '<expr>'],
        ['<expr>', '*', '<expr>'],
        ['<expr>', '/', '<expr>'],
        ['(', '<expr>', ')'],
        ['<integer>']],
    '<integer>': [
        ['<digits>']],
    '<digits>': [
        ['<digit>','<digits>'],
        ['<digit>']],
    '<digit>': [["%s" % str(i)] for i in range(10)],
}

sample_grammar = {
    '<start>': [['<A>','<B>']],
    '<A>': [['a', '<B>', 'c'], ['a', '<A>']],
    '<B>': [['b', '<C>'], ['<D>']],
    '<C>': [['c']],
    '<D>': [['d']]
}

class Column:
    def __init__(self, index, letter):
        self.index, self.letter = index, letter
        self.states, self._unique = [], {}

    def __str__(self):
        return "%s chart[%d]\n%s" % (self.letter, self.index, "\n".join(
            str(state) for state in self.states if state.finished()))

    def add(self, state):
        if state in self._unique:
            return self._unique[state]
        self._unique[state] = state
        self.states.append(state)
        state.e_col = self
        return self._unique[state]


class State:
    def __init__(self, name, expr, dot, s_col, e_col=None):
        self.name, self.expr, self.dot = name, expr, dot
        self.s_col, self.e_col = s_col, e_col

    def finished(self):
        return self.dot >= len(self.expr)

    def at_dot(self):
        return self.expr[self.dot] if self.dot < len(self.expr) else None

    def __str__(self):
        def idx(var):
            return var.index if var else -1

        return self.name + ':= ' + ' '.join([
            str(p)
            for p in [*self.expr[:self.dot], '|', *self.expr[self.dot:]]
        ]) + "(%d,%d)" % (idx(self.s_col), idx(self.e_col))

    def copy(self):
        return State(self.name, self.expr, self.dot, self.s_col, self.e_col)

    def _t(self):
        return (self.name, self.expr, self.dot, self.s_col.index)

    def __hash__(self):
        return hash(self._t())

    def __eq__(self, other):
        return self._t() == other._t()

    def advance(self):
        return State(self.name, self.expr, self.dot + 1, self.s_col)

# The convenience methods `finished()`, `advance()` and `at_dot()` should be
# self explanatory. For example,

# ## Parser
#
# We start with a bare minimum interface for a parser. It should allow one
# to parse a given text using a given nonterminal (which should be present in
# the grammar).

class Parser:
    def recognize_on(self, text, start_symbol):
        raise NotImplemented()

    def parse_on(self, text, start_symbol):
        raise NotImplemented()

# We now initialize the Earley parser, which is a parser.

class EarleyParser(Parser):
    def __init__(self, grammar, log = False, **kwargs):
        self._grammar = grammar
        self.epsilon = nullable(grammar)
        self.log = log

# #### Nullable
#
# Earley parser handles *nullable* nonterminals separately. A nullable
# nonterminal is a nonterminal that can derive an empty string. That is
# at least one of the expansion rules must derive an empty string. An
# expansion rule derives an empty string if *all* of the tokens can
# derive the empty string. This means no terminal symbols (assuming we
# do not have zero width terminal symbols), and all nonterminal symbols
# can derive empty string.
#
# In this implementation, we first initialize the list of first level
# nullable nonterminals that contain an empty expansion. That is, they
# directly derive the empty string.
# Next, we remove any expansion rule that contains a token as these
# expansion rules will not result in empty strings. Next, we start with
# our current list of nullable nonterminals, take one at a time, and
# remove them from the current expansion rules. If any expansion rule
# becomes empty, the corresponding nonterminal is added to the nullable
# nonterminal list. This continues until all nullable nonterminals
# are processed.

def is_nt(k):
    return (k[0], k[-1]) == ('<', '>')

def rem_terminals(g):
    g_cur = {}
    for k in g:
        alts = []
        for alt in g[k]:
            ts = [t for t in alt if not is_nt(t)]
            if not ts:
                alts.append(alt)
        if alts:
            g_cur[k] = alts
    return g_cur

def nullable(g):
    nullable_keys = {k for k in g if [] in g[k]}

    unprocessed  = list(nullable_keys)

    g_cur = rem_terminals(g)
    while unprocessed:
        nxt, *unprocessed = unprocessed
        g_nxt = {}
        for k in g_cur:
            g_alts = []
            for alt in g_cur[k]:
                alt_ = [t for t in alt if t != nxt]
                if not alt_:
                    nullable_keys.add(k)
                    unprocessed.append(k)
                    break
                else:
                    g_alts.append(alt_)
            if g_alts:
                g_nxt[k] = g_alts
        g_cur = g_nxt

    return nullable_keys


class EarleyParser(EarleyParser):
    def chart_parse(self, tokens, start, alts):
        chart = [self.create_column(i, tok) for i, tok in enumerate([None, *tokens])]
        for alt in alts:
            chart[0].add(self.create_state(start, tuple(alt), 0, chart[0]))
        return self.fill_chart(chart)

    def create_column(self, i, tok): return Column(i, tok)

    def create_state(self, sym, alt, num, col): return State(sym, alt, num, col)

# We seed our initial state in the example



class EarleyParser(EarleyParser):
    def predict(self, col, sym, state):
        for alt in self._grammar[sym]:
            col.add(self.create_state(sym, tuple(alt), 0, col))
        if sym in self.epsilon:
            col.add(state.advance())


class EarleyParser(EarleyParser):
    def scan(self, col, state, letter):
        if letter == col.letter:
            col.add(state.advance())


class EarleyParser(EarleyParser):
    def complete(self, col, state):
        parent_states = [st for st in state.s_col.states
                 if st.at_dot() == state.name]
        for st in parent_states:
            col.add(st.advance())


# You can see that the two states are waiting on `<A>` and `<B>`
# respectively at `at_dot()`.
# Hence, we run predict again to add the corresponding rules of `<A>` and `<B>`
# to the current column.


# As you can see, we have a list of states that are waiting
# for `b`, `a` and `d`.

# Our next letter is:


# As we expected, only `<D>` could advance to the next column (`chart[2]`)
# after reading `d`

# Finally, we use complete, so that we can advance the parents of the `<D>` state above.


class EarleyParser(EarleyParser):
    def fill_chart(self, chart):
        for i, col in enumerate(chart):
            for state in col.states:
                if state.finished():
                    self.complete(col, state)
                else:
                    sym = state.at_dot()
                    if sym in self._grammar:
                        self.predict(col, sym, state)
                    else:
                        if i + 1 >= len(chart):
                            continue
                        self.scan(chart[i + 1], state, sym)
            if self.log: print(col, '\n')
        return chart

# We can now recognize the given string as part of the language represented by the grammar.


# The chart above only shows completed entries. The parenthesized expression
# indicates the column just before the first character was recognized, and the
# ending column.

# Notice how the `<start>` nonterminal shows the dot at the end. That is, fully parsed.

# ## Derivation trees
#
# We use the following procedures to translate the parse forest to individual
# trees.

# ### parse_prefix

class EarleyParser(EarleyParser):
    def parse_prefix(self, text, start_symbol):
        alts = [tuple(alt) for alt in self._grammar[start_symbol]]
        self.table = self.chart_parse(text, start_symbol, alts)
        for col in reversed(self.table):
            states = [st for st in col.states
                if st.name == start_symbol and st.expr in alts and st.s_col.index == 0
            ]
            if states:
                return col.index, states
        return -1, []


# ### parse_on
#
# Our `parse_on()` method is slightly different from usual Earley implementations
# in that we accept any nonterminal symbol, not just nonterminal symbols with a
# single expansion rule. We accomplish this by computing a different chart for
# each expansion.

class EarleyParser(EarleyParser):
    def parse_on(self, text, start_symbol):
        print("parse_on method started")
        starts = self.recognize_on(text, start_symbol)
        print("recognize_on method finished")
        forest = self.parse_forest(self.table, starts)
        for tree in self.extract_trees(forest):
            yield tree

    def recognize_on(self, text, start_symbol):
        #print("recognize_on method started")
        cursor, states = self.parse_prefix(text, start_symbol)
        starts = [s for s in states if s.finished()]

        if cursor < len(text) or not starts:
            raise SyntaxError("at " + repr(text[cursor:]))
        return starts

# ### parse_paths
#
#
# The parse_paths() method tries to unify the given expression in `named_expr` with
# the parsed string. For that, it extracts the last symbol in `named_expr` and
# checks if it is a terminal symbol. If it is, then it checks the chart at `til` to
# see if the letter corresponding to the position matches the terminal symbol.
# If it does, extend our start index by the length of the symbol.
#
# If the symbol was a nonterminal symbol, then we retrieve the parsed states
# at the current end column index (`til`) that correspond to the nonterminal
# symbol, and collect the start index. These are the end column indexes for
# the remaining expression.
#
# Given our list of start indexes, we obtain the parse paths from the remaining
# expression. If we can obtain any, then we return the parse paths. If not, we
# return an empty list.

class EarleyParser(EarleyParser):
    def parse_paths(self, named_expr, chart, frm, til):
        def paths(state, start, k, e):
            if not e:
                return [[(state, k)]] if start == frm else []
            else:
                return [[(state, k)] + r
                        for r in self.parse_paths(e, chart, frm, start)]

        *expr, var = named_expr
        starts = None
        if var not in self._grammar:
            starts = ([(var, til - len(var),
                        't')] if til > 0 and chart[til].letter == var else [])
        else:
            starts = [(s, s.s_col.index, 'n') for s in chart[til].states
                      if s.finished() and s.name == var]

        return [p for s, start, k in starts for p in paths(s, start, k, expr)]


class EarleyParser(EarleyParser):
    def forest(self, s, kind, chart):
        return self.parse_forest(chart, [s]) if kind == 'n' else (s, [])

    def _parse_forest(self, chart, state):
        pathexprs = self.parse_paths(state.expr, chart, state.s_col.index,
                                     state.e_col.index) if state.expr else []
        return (state.name, [[(v, k, chart) for v, k in reversed(pathexpr)]
                            for pathexpr in pathexprs])

    def parse_forest(self, chart, states):
        names = list({s.name for s in states})
        assert len(names) == 1
        forest = [self._parse_forest(chart, state) for state in states]
        return (names[0], [e for name, expr in forest for e in expr])


# ### extract_trees
#
# We show how to extract a single tree first, and then generalize it to
# all trees.

class EarleyParser(EarleyParser):
    def extract_a_tree(self, forest_node):
        name, paths = forest_node
        if not paths:
            return (name, [])
        return (name, [self.extract_a_tree(self.forest(*p)) for p in paths[0]])

    def extract_trees(self, forest):
        yield self.extract_a_tree(forest)

# We need a way to display parse trees.

import itertools as I

class O:
    def __init__(self, **keys): self.__dict__.update(keys)
    def __repr__(self): return str(self.__dict__)

Options = O(F='|', L='+', V='|', H='-', NL='\n')

def format_newlines(prefix, formatted_node):
    replacement = ''.join([Options.NL, '\n', prefix])
    return formatted_node.replace('\n', replacement)

def format_tree(node, format_node, get_children, prefix=''):
    children = list(get_children(node))
    next_prefix = ''.join([prefix, Options.V, '   '])
    for child in children[:-1]:
        fml = format_newlines(next_prefix, format_node(child))
        yield ''.join([prefix, Options.F, Options.H, Options.H, ' ', fml])
        tree = format_tree(child, format_node, get_children, next_prefix)
        for result in tree:
            yield result
    if children:
        last_prefix = ''.join([prefix, '    '])
        fml = format_newlines(last_prefix, format_node(children[-1]))
        yield ''.join([prefix, Options.L, Options.H, Options.H, ' ', fml])
        tree = format_tree(children[-1], format_node, get_children, last_prefix)
        for result in tree:
            yield result

def format_parsetree(node,
          format_node=lambda x: repr(x[0]),
          get_children=lambda x: x[1]):
    lines = I.chain([format_node(node)], format_tree(node, format_node, get_children), [''],)
    return '\n'.join(lines)


# ### Ambiguous Parsing
#
# Ambiguous grammars can produce multiple derivation trees for some given string.
# In the above example, the `a_grammar` can parse `1+2+4` in as either `[1+2]+4` or `1+[2+4]`.
#
# That is, we need to extract all derivation trees.
# We enhance our `extract_trees()` as below.
#

class EarleyParser(EarleyParser):
    def extract_trees(self, forest_node):
        name, paths = forest_node
        if not paths:
            yield (name, [])
        results = []
        for path in paths:
            ptrees = [self.extract_trees(self.forest(*p)) for p in path]
            for p in I.product(*ptrees):
                yield (name, p)
# ## Example
#


# ## Almost infinite parse trees
#
# There is a problem with our `extract_trees()` method. The issue is that it is
# too eager. The parse forest can have an infinite number of trees, and at this
# time we effectively try to extract all at the same time. So, in case of
# such grammars our `extract_trees()` will fail. Here are two example grammars.



import random

class SimpleExtractor:
    def __init__(self, parser, text, start_symbol):
        self.parser = parser
        cursor, states = parser.parse_prefix(text, start_symbol)
        starts = [s for s in states if s.finished()]
        if cursor < len(text) or not starts:
            raise SyntaxError("at " + repr(cursor))
        self.my_forest = parser.parse_forest(parser.table, starts)

    def extract_a_node(self, forest_node):
        name, paths = forest_node
        if not paths:
            return ((name, 0, 1), []), (name, [])
        cur_path, i, l = self.choose_path(paths)
        child_nodes = []
        pos_nodes = []
        for s, kind, chart in cur_path:
            f = self.parser.forest(s, kind, chart)
            postree, ntree = self.extract_a_node(f)
            child_nodes.append(ntree)
            pos_nodes.append(postree)

        return ((name, i, l), pos_nodes), (name, child_nodes)

    def choose_path(self, arr):
        l = len(arr)
        i = random.randrange(l)
        return arr[i], i, l

    def extract_a_tree(self):
        pos_tree, parse_tree = self.extract_a_node(self.my_forest)
        return parse_tree

# At this point, we also need a simple way to collapse the derivation tree to the original string

def tree_to_str(tree):
    expanded = []
    to_expand = [tree]
    while to_expand:
        (key, children, *rest), *to_expand = to_expand
        if is_nt(key):
            to_expand = list(children) + list(to_expand)
        else:
            assert not children
            expanded.append(key)
    return ''.join(expanded)
#

# However, `SimpleExtractor` has a problem. The issue is that since we rely on
# randomness for exploration, it gives no guarantees on the uniqueness of the
# returned trees. Hence, we need a way to keep track of the explored paths.
# our next class `EnahncedExtractor` can do that. In `EnhancedExtractor`,
# different exploration paths form a tree of nodes.
#
# First we define a data-structure to keep track of explorations.
# * `_chosen` contains the current choice
# * `next` holds the next choice done using `_chosen`
# * `total` holds he total number of choices for this node.

class ChoiceNode:
    def __init__(self, parent, total):
        self._p, self._chosen = parent, 0
        self._total, self.next = total, None

    def chosen(self):
        assert not self.finished()
        return self._chosen

    def __str__(self):
        return '%d(%s/%s %s)' % (self._i, str(self._chosen),
                                 str(self._total), str(self.next))
    def __repr__(self):
        return repr((self._i, self._chosen, self._total))

    def increment(self):
        # as soon as we increment, next becomes invalid
        self.next = None
        self._chosen += 1
        if self.finished():
            if self._p is None:
                return None
            return self._p.increment()
        return self

    def finished(self):
        return self._chosen >= self._total

# Initialization of the data-structure in the constructor.

class EnhancedExtractor(SimpleExtractor):
    def __init__(self, parser, text, start_symbol):
        super().__init__(parser, text, start_symbol)
        self.choices = choices = ChoiceNode(None, 1)

# Given an array and a choice node, `choose_path()` returns the element
# in array corresponding to the next choice node if it exists, or produces
# a new choice nodes, and returns that element.

class EnhancedExtractor(EnhancedExtractor):
    def choose_path(self, arr, choices):
        arr_len = len(arr)
        if choices.next is not None:
            if choices.next.finished():
                return None, None, None, choices.next
        else:
            choices.next = ChoiceNode(choices, arr_len)
        next_choice = choices.next.chosen()
        choices = choices.next
        return arr[next_choice], next_choice, arr_len, choices


class EnhancedExtractor(EnhancedExtractor):
    def extract_a_node(self, forest_node, seen, choices):
        name, paths = forest_node
        if not paths:
            return (name, []), choices

        cur_path, _i, _l, new_choices = self.choose_path(paths, choices)
        if cur_path is None:
            return None, new_choices
        child_nodes = []
        for s, kind, chart in cur_path:
            if kind == 't':
                child_nodes.append((s, []))
                continue
            nid = (s.name, s.s_col.index, s.e_col.index)
            if nid in seen:
                return None, new_choices
            f = self.parser.forest(s, kind, chart)
            ntree, newer_choices = self.extract_a_node(f, seen | {nid}, new_choices)
            if ntree is None:
                return None, newer_choices
            child_nodes.append(ntree)
            new_choices = newer_choices
        return (name, child_nodes), new_choices

# The `extract_a_tree()` is a depth first extractor of a single tree. It tries to
# extract a tree, and if the extraction returns None, it means that a particular
# choice was exhausted, or we hit on a recursion. In that case, we increment the
# choice, and explore a new path.

class EnhancedExtractor(EnhancedExtractor):
    def extract_a_tree(self):
        while not self.choices.finished():
            parse_tree, choices = self.extract_a_node(self.my_forest, set(), self.choices)
            choices.increment()
            if parse_tree is not None:
                return parse_tree
        return None

# Note that the `EnhancedExtractor` only extracts nodes that are not directly
# recursive. That is, if it finds a node with a nonterminal that covers the same
# span as that of a parent node with the same nonterminal, it skips the node.

class EarleyParser(EarleyParser):
    def earley_complete(self, col, state):
        parent_states = [st for st in state.s_col.states
                 if st.at_dot() == state.name]
        for st in parent_states:
            col.add(st.advance())

#
class LeoParser(EarleyParser):
    def complete(self, col, state):
        return self.leo_complete(col, state)

    def leo_complete(self, col, state):
        detred = self.deterministic_reduction(state)
        if detred:
            col.add(detred.copy())
        else:
            self.earley_complete(col, state)

    def deterministic_reduction(self, state):
        raise NotImplemented()

class Column(Column):
    def __init__(self, index, letter):
        self.index, self.letter = index, letter
        self.states, self._unique, self.transitives = [], {}, {}

    def add_transitive(self, key, state):
        assert key not in self.transitives
        self.transitives[key] = state
        return self.transitives[key]



class LeoParser(LeoParser):
    def uniq_postdot(self, st_A):
        col_s1 = st_A.s_col
        parent_states = [
            s for s in col_s1.states if s.expr and s.at_dot() == st_A.name
        ]
        if len(parent_states) > 1:
            return None
        matching_st_B = [s for s in parent_states if s.dot == len(s.expr) - 1]
        return matching_st_B[0] if matching_st_B else None

    def get_top(self, state_A):
        st_B_inc = self.uniq_postdot(state_A)
        if not st_B_inc:
            return None

        t_name = st_B_inc.name
        if t_name in st_B_inc.e_col.transitives:
            return st_B_inc.e_col.transitives[t_name]

        st_B = st_B_inc.advance()

        top = self.get_top(st_B) or st_B
        return st_B_inc.e_col.add_transitive(t_name, top)

    def deterministic_reduction(self, state):
        return self.get_top(state)


# We have fixed the complexity bounds. However, because we are saving only the topmost item of a right recursion, we need to fix our parser to be aware of our fix while extracting parse trees.
#
# We first change the definition of `add_transitive()` so that results of deterministic reduction can be identified later.

class Column(Column):
    def add_transitive(self, key, state):
        assert key not in self.transitives
        self.transitives[key] = self.create_tstate(state)
        return self.transitives[key]

    def create_tstate(self, state):
        return TState(state.name, state.expr, state.dot, state.s_col, state.e_col)


# We also need a `back()` method to create the constraints.

class State(State):
    def back(self):
        return TState(self.name, self.expr, self.dot - 1, self.s_col, self.e_col)

# We update `copy()` to make `TState` items instead.

class TState(State):
    def copy(self):
        return TState(self.name, self.expr, self.dot, self.s_col, self.e_col)


class LeoParser(LeoParser):
    def __init__(self, grammar, **kwargs):
        super().__init__(grammar, **kwargs)
        self._postdots = {}

    def uniq_postdot(self, st_A):
        col_s1 = st_A.s_col
        parent_states = [
            s for s in col_s1.states if s.expr and s.at_dot() == st_A.name
        ]
        if len(parent_states) > 1:
            return None
        matching_st_B = [s for s in parent_states if s.dot == len(s.expr) - 1]
        if matching_st_B:
            self._postdots[matching_st_B[0]._t()] = st_A
            return matching_st_B[0]
        return None

    def expand_tstate(self, state, e):
        if state._t() not in self._postdots:
            return
        c_C = self._postdots[state._t()]
        e.add(c_C.advance())
        self.expand_tstate(c_C.back(), e)

    def rearrange(self, table):
        f_table = [self.create_column(c.index, c.letter) for c in table]
        for col in table:
            for s in col.states:
                f_table[s.s_col.index].states.append(s)
        return f_table

    def parse_on(self, text, start_symbol):
        starts = self.recognize_on(text, start_symbol)
        self.r_table = self.rearrange(self.table)
        forest = self.parse_forest(self.table, starts)
        for tree in self.extract_trees(forest):
            yield tree

    def parse_forest(self, chart, states):
        for state in states:
            if isinstance(state, TState):
                self.expand_tstate(state.back(), state.e_col)

        return super().parse_forest(chart, states)



# This completes our implementation of `LeoParser `.

import json
import sys

def check(inp, program):
    # reading the data from the file
    with open('../../handwritten/%s.json' % program) as f:
        data = f.read()
    output_grammar = json.loads(data)
    ee = EarleyParser(output_grammar).recognize_on(inp, START)

