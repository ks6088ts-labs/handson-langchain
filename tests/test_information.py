from api.settings import information


def test_settings():
    settings = information.InformationSettings()
    assert "version" in settings.dict().keys()
    assert "revision" in settings.dict().keys()
