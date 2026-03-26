import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_create_question_with_invalid_points():
    with pytest.raises(Exception):
        Question(title='q1', points=0)
    with pytest.raises(Exception):
        Question(title='q1', points=101)
    with pytest.raises(Exception):
        Question(title='q1', points=-5)

def test_create_choice_with_invalid_text():
    question = Question(title='q1')
    
    with pytest.raises(Exception):
        question.add_choice('')
    with pytest.raises(Exception):
        question.add_choice('a' * 101)

def test_add_multiple_choices():
    question = Question(title='q1')
    
    question.add_choice('choice A')
    question.add_choice('choice B')
    question.add_choice('choice C')
    
    assert len(question.choices) == 3
    assert question.choices[0].text == 'choice A'
    assert question.choices[1].text == 'choice B'
    assert question.choices[2].text == 'choice C'

def test_remove_choice_by_id():
    question = Question(title='q1')
    
    question.add_choice('choice A')
    question.add_choice('choice B')
    question.add_choice('choice C')
    
    question.remove_choice_by_id(2)
    
    assert len(question.choices) == 2
    assert question.choices[0].id == 1
    assert question.choices[1].id == 3

def test_remove_all_choices():
    question = Question(title='q1')
    
    question.add_choice('choice A')
    question.add_choice('choice B')
    question.add_choice('choice C')
    
    question.remove_all_choices()
    
    assert len(question.choices) == 0

def test_set_correct_choices():
    question = Question(title='q1')
    
    question.add_choice('choice A')
    question.add_choice('choice B')
    question.add_choice('choice C')
    
    question.set_correct_choices([2])
    
    assert not question.choices[0].is_correct
    assert question.choices[1].is_correct
    assert not question.choices[2].is_correct

def test_correct_selected_choices_filters_only_correct():
    question = Question(title='q1', max_selections=3)
    
    question.add_choice('choice A')
    question.add_choice('choice B')
    question.add_choice('choice C')
    question.set_correct_choices([1, 3])
    
    correct_answers = question.correct_selected_choices([1, 2, 3])
    
    assert correct_answers == [1, 3]

def test_correct_selected_choices_exceeds_max_selections():
    question = Question(title='q1', max_selections=2)
    
    question.add_choice('choice A')
    question.add_choice('choice B')
    question.add_choice('choice C')
    
    with pytest.raises(Exception):
        question.correct_selected_choices([1, 2, 3])

def test_add_choice_returns_choice_object():
    question = Question(title='q1')
    
    returned_choice = question.add_choice('choice A', True)
    
    assert returned_choice.text == 'choice A'
    assert returned_choice.is_correct == True
    assert returned_choice.id == 1

def test_choice_is_correct_defaults_to_false():
    question = Question(title='q1')
    
    question.add_choice('choice A')
    
    assert question.choices[0].is_correct == False