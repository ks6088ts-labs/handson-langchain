from api.settings import information


def test_settings():
    settings = information.InformationSettings()
    assert "version" in settings.model_dump().keys()
    assert "revision" in settings.model_dump().keys()
