# drules_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def function1_tray(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'its_aids', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function1_tray: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function11_tray(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'its_aids', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function11_tray: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'any_disese', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function2: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (3,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'any_disese', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function3: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (4,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'any_disese', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function4: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function6(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'any_disese', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function6: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function5(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'any_disese2', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function5: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function7(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'any_disese2', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function7: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function8(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'any_disese2', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function8: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (3,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function9(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'its_Hepatitis_b', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function9: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function99(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'its_Hepatitis_b', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function99: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function10(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'its_Rheumatoid_Arthritis', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function10: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function1010(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'its_Rheumatoid_Arthritis', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function1010: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function11(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'any_disese3', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function11: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function13(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'any_disese3', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function13: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function14(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'any_disese3', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function14: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (3,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function15(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'any_disese3', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function15: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (4,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function12(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'its_Gout', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function12: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function1212(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'its_Gout', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function1212: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function16(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'any_disese4', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function16: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function17(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'any_disese4', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function17: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function18(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'any_disese4', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function18: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (3,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function19(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'any_disese4', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function19: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (4,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def function20(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('dquestion', 'any_disese4', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "drules.function20: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (5,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('drules')
  
  bc_rule.bc_rule('function1_tray', This_rule_base, 'you_have_a_disease',
                  function1_tray, None,
                  (pattern.pattern_literal("it's aids"),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('function11_tray', This_rule_base, 'you_have_a_disease',
                  function11_tray, None,
                  (pattern.pattern_literal("Ohhh shiiit you are good :("),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('function2', This_rule_base, 'you_have_a_disease',
                  function2, None,
                  (pattern.pattern_literal("Allergies"),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('function3', This_rule_base, 'you_have_a_disease',
                  function3, None,
                  (pattern.pattern_literal("Type1diabetes"),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('function4', This_rule_base, 'you_have_a_disease',
                  function4, None,
                  (pattern.pattern_literal("Type2diabetes"),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('function6', This_rule_base, 'you_have_a_disease',
                  function6, None,
                  (pattern.pattern_literal("COVID-19"),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('function5', This_rule_base, 'you_have_a_disease',
                  function5, None,
                  (pattern.pattern_literal("Normal blood pressure"),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('function7', This_rule_base, 'you_have_a_disease',
                  function7, None,
                  (pattern.pattern_literal("Common Cold"),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('function8', This_rule_base, 'you_have_a_disease',
                  function8, None,
                  (pattern.pattern_literal("Kidney stone"),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('function9', This_rule_base, 'you_have_a_disease',
                  function9, None,
                  (pattern.pattern_literal("Hepatitis_b"),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('function99', This_rule_base, 'you_have_a_disease',
                  function99, None,
                  (pattern.pattern_literal("Ohhh shiiit you are good :("),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('function10', This_rule_base, 'you_have_a_disease',
                  function10, None,
                  (pattern.pattern_literal("Rheumatoid Arthritis"),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('function1010', This_rule_base, 'you_have_a_disease',
                  function1010, None,
                  (pattern.pattern_literal("Ohhh shiiit you are good :("),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('function11', This_rule_base, 'you_have_a_disease',
                  function11, None,
                  (pattern.pattern_literal("Chronic kidney"),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('function13', This_rule_base, 'you_have_a_disease',
                  function13, None,
                  (pattern.pattern_literal("glaucoma"),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('function14', This_rule_base, 'you_have_a_disease',
                  function14, None,
                  (pattern.pattern_literal("Leukemia"),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('function15', This_rule_base, 'you_have_a_disease',
                  function15, None,
                  (pattern.pattern_literal("Anemia"),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('function12', This_rule_base, 'you_have_a_disease',
                  function12, None,
                  (pattern.pattern_literal("Gout"),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('function1212', This_rule_base, 'you_have_a_disease',
                  function1212, None,
                  (pattern.pattern_literal("Ohhh shiiit you are good :("),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('function16', This_rule_base, 'you_have_a_disease',
                  function16, None,
                  (pattern.pattern_literal("Heart attack"),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('function17', This_rule_base, 'you_have_a_disease',
                  function17, None,
                  (pattern.pattern_literal("Hypothyroidism"),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('function18', This_rule_base, 'you_have_a_disease',
                  function18, None,
                  (pattern.pattern_literal("Colon Cancer"),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('function19', This_rule_base, 'you_have_a_disease',
                  function19, None,
                  (pattern.pattern_literal("Osteoarthritis"),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('function20', This_rule_base, 'you_have_a_disease',
                  function20, None,
                  (pattern.pattern_literal("Favism"),),
                  (),
                  (contexts.variable('ans'),))


Krb_filename = '..\\drules.krb'
Krb_lineno_map = (
    ((16, 20), (3, 3)),
    ((22, 27), (5, 5)),
    ((40, 44), (8, 8)),
    ((46, 51), (10, 10)),
    ((64, 68), (13, 13)),
    ((70, 75), (15, 15)),
    ((76, 76), (16, 16)),
    ((89, 93), (19, 19)),
    ((95, 100), (21, 21)),
    ((101, 101), (22, 22)),
    ((114, 118), (25, 25)),
    ((120, 125), (27, 27)),
    ((126, 126), (28, 28)),
    ((139, 143), (31, 31)),
    ((145, 150), (33, 33)),
    ((151, 151), (34, 34)),
    ((164, 168), (37, 37)),
    ((170, 175), (39, 39)),
    ((176, 176), (40, 40)),
    ((189, 193), (43, 43)),
    ((195, 200), (45, 45)),
    ((201, 201), (46, 46)),
    ((214, 218), (49, 49)),
    ((220, 225), (51, 51)),
    ((226, 226), (52, 52)),
    ((239, 243), (55, 55)),
    ((245, 250), (57, 57)),
    ((263, 267), (60, 60)),
    ((269, 274), (62, 62)),
    ((287, 291), (65, 65)),
    ((293, 298), (67, 67)),
    ((311, 315), (70, 70)),
    ((317, 322), (72, 72)),
    ((335, 339), (75, 75)),
    ((341, 346), (77, 77)),
    ((347, 347), (78, 78)),
    ((360, 364), (81, 81)),
    ((366, 371), (83, 83)),
    ((372, 372), (84, 84)),
    ((385, 389), (87, 87)),
    ((391, 396), (89, 89)),
    ((397, 397), (90, 90)),
    ((410, 414), (93, 93)),
    ((416, 421), (95, 95)),
    ((422, 422), (96, 96)),
    ((435, 439), (99, 99)),
    ((441, 446), (101, 101)),
    ((459, 463), (104, 104)),
    ((465, 470), (106, 106)),
    ((483, 487), (109, 109)),
    ((489, 494), (111, 111)),
    ((495, 495), (112, 112)),
    ((508, 512), (115, 115)),
    ((514, 519), (117, 117)),
    ((520, 520), (118, 118)),
    ((533, 537), (121, 121)),
    ((539, 544), (123, 123)),
    ((545, 545), (124, 124)),
    ((558, 562), (127, 127)),
    ((564, 569), (129, 129)),
    ((570, 570), (130, 130)),
    ((583, 587), (133, 133)),
    ((589, 594), (135, 135)),
    ((595, 595), (136, 136)),
)
