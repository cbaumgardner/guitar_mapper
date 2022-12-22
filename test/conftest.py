import pytest

@pytest.fixture
def expected_default_neck():
    return {1: '<span class="string-tuning note"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">F#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">G#</span></span><span class="string-tab note root inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">C#</span></span><span class="string-tab note"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">F#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">G#</span></span><span class="string-tab note root inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">C#</span></span><span class="string-tab note"><span class="note-indicator">D</span></span>', 
            2: '<span class="string-tuning note"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab note inlay"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">F#</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">G#</span></span><span class="string-tab note root"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab note inlay"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">F#</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">G#</span></span><span class="string-tab note root"><span class="note-indicator">A</span></span>', 
            3: '<span class="string-tuning">G</span><span class="string-tab note"><span class="note-indicator">G#</span></span><span class="string-tab note root"><span class="note-indicator">A</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">B</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab note inlay"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">F#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">G#</span></span><span class="string-tab note root"><span class="note-indicator">A</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">B</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab note inlay"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span>', 
            4: '<span class="string-tuning note"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">E</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">F#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">G#</span></span><span class="string-tab note root inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab note inlay"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">E</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">F#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">G#</span></span><span class="string-tab note root inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span>', 
            5: '<span class="string-tuning note root"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">B</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab note inlay"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">F#</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">G#</span></span><span class="string-tab note root inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">B</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab note inlay"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">F#</span></span><span class="string-tab">&nbsp;</span>', 
            6: '<span class="string-tuning note"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">F#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">G#</span></span><span class="string-tab note root inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">C#</span></span><span class="string-tab note"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">F#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">G#</span></span><span class="string-tab note root inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">C#</span></span><span class="string-tab note"><span class="note-indicator">D</span></span>'}

@pytest.fixture
def expected_g_lydian_neck():
    return {1: '<span class="string-tuning note"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">F#</span></span><span class="string-tab note root inlay"><span class="note-indicator">G</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">C#</span></span><span class="string-tab note"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">F#</span></span><span class="string-tab note root inlay"><span class="note-indicator">G</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">C#</span></span><span class="string-tab note"><span class="note-indicator">D</span></span>', 
            2: '<span class="string-tuning note"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab note inlay"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">F#</span></span><span class="string-tab note root"><span class="note-indicator">G</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab note inlay"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">F#</span></span><span class="string-tab note root"><span class="note-indicator">G</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">A</span></span>', 
            3: '<span class="string-tuning note root"><span class="note-indicator">G</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">A</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">B</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab note inlay"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">F#</span></span><span class="string-tab note root inlay"><span class="note-indicator">G</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">A</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">B</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab note inlay"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span>', 
            4: '<span class="string-tuning note"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">E</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">F#</span></span><span class="string-tab note root inlay"><span class="note-indicator">G</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab note inlay"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">E</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">F#</span></span><span class="string-tab note root inlay"><span class="note-indicator">G</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span>', 
            5: '<span class="string-tuning note"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">B</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab note inlay"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">F#</span></span><span class="string-tab note root"><span class="note-indicator">G</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">B</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab note inlay"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">F#</span></span><span class="string-tab note root"><span class="note-indicator">G</span></span>', 
            6: '<span class="string-tuning note"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">F#</span></span><span class="string-tab note root inlay"><span class="note-indicator">G</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">C#</span></span><span class="string-tab note"><span class="note-indicator">D</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">F#</span></span><span class="string-tab note root inlay"><span class="note-indicator">G</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">C#</span></span><span class="string-tab note"><span class="note-indicator">D</span></span>'}


@pytest.fixture
def expected_f_sharp_minor_pentatonic():
    return {1: '<span class="string-tuning note"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note root"><span class="note-indicator">F#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">C#</span></span><span class="string-tab">&nbsp;</span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note root"><span class="note-indicator">F#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">C#</span></span><span class="string-tab">&nbsp;</span>', 
            2: '<span class="string-tuning note"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note root inlay"><span class="note-indicator">F#</span></span><span class="string-tab">&nbsp;</span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note root inlay"><span class="note-indicator">F#</span></span><span class="string-tab">&nbsp;</span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">A</span></span>', 
            3: '<span class="string-tuning">G</span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">A</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">B</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note root"><span class="note-indicator">F#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">A</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">B</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span>', 
            4: '<span class="string-tuning">D</span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">E</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note root"><span class="note-indicator">F#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">E</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note root"><span class="note-indicator">F#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span>', 
            5: '<span class="string-tuning note"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">B</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note root inlay"><span class="note-indicator">F#</span></span><span class="string-tab">&nbsp;</span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note"><span class="note-indicator">B</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab note"><span class="note-indicator">C#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note root inlay"><span class="note-indicator">F#</span></span><span class="string-tab">&nbsp;</span>', 
            6: '<span class="string-tuning note"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note root"><span class="note-indicator">F#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">C#</span></span><span class="string-tab">&nbsp;</span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">E</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note root"><span class="note-indicator">F#</span></span><span class="string-tab inlay">&nbsp;</span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">A</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">B</span></span><span class="string-tab">&nbsp;</span><span class="string-tab note inlay"><span class="note-indicator">C#</span></span><span class="string-tab">&nbsp;</span>'}