import random
from utils import swap_words

def test_swap_words():
    # Test case 1: No words should be swapped
    sentence = "Hello, world!"
    probability = 0.0
    expected_output = "Hello, world!"
    assert swap_words(sentence, probability) == expected_output, f"Expected: {expected_output}, got: {swap_words(sentence, probability)}"

    # Test case 2: Half of the words should be swapped
    sentence = "Hello, world!"
    probability = 0.5
    expected_output = "world, Hello!"
    assert swap_words(sentence, probability) == expected_output, f"Expected: {expected_output}, got: {swap_words(sentence, probability)}"

    # Test case 3: All words should be swapped
    sentence = "Hello, world!"
    probability = 1.0
    expected_output = "world, Hello!"
    assert swap_words(sentence, probability) == expected_output, f"Expected: {expected_output}, got: {swap_words(sentence, probability)}"

    # Test case 3.5: Even number of words should be swapped
    sentence = "Hello, world! bar"
    probability = 1.0
    expected_output = ["world, Hello! bar", "bar, world! Hello", "Hello, bar! world"]
    assert swap_words(sentence, probability) in expected_output, f"Expected: {expected_output}, got: {swap_words(sentence, probability)}"

    # Test case 4: More words to swap
    sentence = "Hello, world!\nNew day"
    probability = 0.5
    expected_outputs = set(["world, Hello!\nNew day", "Hello, day!\nNew world", "Hello, New!\nworld day", "day, New!\nworld Hello", "New, world!\nHello day", "Hello, world!\nday New", "day, world!\nNew Hello"])
    out = swap_words(sentence, probability)
    assert out in expected_outputs, f"Expected: {expected_outputs}, got: {out}"

    probability = 1.0
    expected_output = "New, day!\nHello world"
    out = swap_words(sentence, probability)
    assert out == expected_output, f"Expected: {expected_output}, got: {out}"

test_swap_words()