from scale_chart import FretBoard

def test_draw_neck_default(expected_default_neck):
    fretboard = FretBoard()
    actual = fretboard.draw_neck()
    assert actual == expected_default_neck

def test_draw_neck_g_lydian(expected_g_lydian_neck):
    fretboard = FretBoard("G", "Lydian")
    actual = fretboard.draw_neck()
    assert actual == expected_g_lydian_neck

def test_draw_neck_f_sharp_minor_pentatonic(expected_f_sharp_minor_pentatonic):
    fretboard = FretBoard("F#", "Minor Pentatonic")
    actual = fretboard.draw_neck()
    assert actual == expected_f_sharp_minor_pentatonic