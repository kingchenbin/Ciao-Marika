from nose.tools import *
from lexicon.lexicon import lexicon
from lexicon.parser import *

def test_basic_sentence():
    result = lexicon.scan("bear kill princess")
    assert_equal(result, [('noun', 'bear'),
                          ('verb', 'kill'),
                          ('noun', 'princess')])
    sentence = parse_sentence(result)
    assert_equal(sentence.subject, 'bear')
    assert_equal(sentence.verb, 'kill')
    assert_equal(sentence.object, 'princess')

def test_noisy_sentence():
    result = lexicon.scan("in kill of bear princess")
    assert_equal(result, [('stop', 'in'),
                          ('verb', 'kill'),
                          ('stop', 'of'),
                          ('noun', 'bear'),
                          ('noun', 'princess')])
    sentence = parse_sentence(result)
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'kill')
    assert_equal(sentence.object, 'bear')
