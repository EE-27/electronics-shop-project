from src.keyboard import Keyboard

def test_str():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"

    try:
        kb.language = 'CH'
    except AttributeError as e:
        assert str(e) == "Unsupported language. Supported languages: EN, RU"