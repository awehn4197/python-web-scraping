import re

def extract_wiki_value(input_string):
    # Define a regular expression pattern
    pattern = r'/wiki/(.*)'
    
    # Use re.search to find the match
    match = re.search(pattern, input_string)
    
    # Extract the value if there's a match
    if match:
        return match.group(1)
    else:
        return None

def test_extract_wiki_value():
    # Test cases
    assert extract_wiki_value("/wiki/some_value") == "some_value"
    assert extract_wiki_value("/wiki/another_value") == "another_value"
    assert extract_wiki_value("/invalid_format/") is None
    assert extract_wiki_value("/no_wiki_prefix") is None
    assert extract_wiki_value("/wiki/") == ""
    assert extract_wiki_value("/wiki/another_value/sldkf/sdlkjf") == "another_value/sldkf/sdlkjf"
    assert extract_wiki_value("/wiki/!_(Trippie_Redd_album)") == "!_(Trippie_Redd_album)"


