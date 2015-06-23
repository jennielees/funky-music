""" Simple testing for the Spotify functionality
    so we don't need to click through pages to make
    sure it's working.

    Try this approach to running tests:

    From the command-line, do both of these:
    * pip install nose
    * nosetests

    nosetests automatically finds and runs tests in files starting with test_.
"""

from spotify import get_music


def test_get_happy():
    result = get_music("happy")

    for playlist in result:
        # make sure every playlist has the word 'happy' in its name
        assert 'happy' in playlist.get('name').lower()


def test_get_limit():
    # test that if we have a limit of 20 we get 20 results
    result = get_music('happy', limit=20)
    assert len(result) == 20
