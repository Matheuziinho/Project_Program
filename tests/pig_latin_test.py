from project_program.pig_latin import translate


def test_translate() -> None:
    assert translate("apple") == "appleay"
    assert translate("xray") == "xrayay"
    assert translate("yttria") == "yttriaay"
    assert translate("pig") == "igpay"
    assert translate("chair") == "airchay"
    assert translate("thrush") == "ushthray"
    assert translate("quick") == "ickquay"
    assert translate("square") == "aresquay"
    assert translate("my") == "ymay"
    assert translate("python") == "ythonpay"
    assert translate("rhythm") == "ythmrhay"
