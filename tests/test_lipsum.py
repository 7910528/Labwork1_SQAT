from pages.lipsum_page import LipsumPage


def test_lipsum_ukrainian_has_word_riba(driver):
    page = LipsumPage(driver)

    page.open()

    page.switch_to_ukrainian()

    text = page.get_generated_text()
    assert "риба" in text.lower(), "The generated text does not contain the word 'риба'. Full text: {}".format(text)
