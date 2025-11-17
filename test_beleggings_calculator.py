import pytest
from beleggings_calculator import bereken_saldo


def test_eenmalige_inleg_mag_niet_negatief_zijn():
    with pytest.raises(ValueError):
        bereken_saldo(
            eenmalige_inleg=-100,
            maandelijkse_inleg=50,
            looptijd=10,
            winst_percentage=5,
        )

def test_maandelijkse_inleg_mag_niet_negatief_zijn():
    with pytest.raises(ValueError):
        bereken_saldo(
            eenmalige_inleg=100,
            maandelijkse_inleg=-1,
            looptijd=10,
            winst_percentage=5,
        )

def test_looptijd_moet_groter_dan_nul_zijn():
    with pytest.raises(ValueError):
        bereken_saldo(
            eenmalige_inleg=100,
            maandelijkse_inleg=10,
            looptijd=0,
            winst_percentage=5,
        )

def test_winst_percentage_moet_groter_dan_nul_zijn():
    with pytest.raises(ValueError):
        bereken_saldo(
            eenmalige_inleg=100,
            maandelijkse_inleg=10,
            looptijd=10,
            winst_percentage=0,
        )

def test_winst_percentage_mag_niet_groter_dan_honderd_zijn():
    with pytest.raises(ValueError):
        bereken_saldo(
            eenmalige_inleg=100,
            maandelijkse_inleg=10,
            looptijd=10,
            winst_percentage=101,
        )

def test_enkel_eenmalige_inleg():
    saldo, totale_inleg, winst = bereken_saldo(
        eenmalige_inleg=1000,
        maandelijkse_inleg=0,
        looptijd=1,
        winst_percentage=5,
    )
    assert round(totale_inleg, 2) == 1000
    assert round(saldo, 2) == 1050
    assert round(winst, 2) == 50

def test_1_jaar_met_maandelijkse_inleg():
    saldo, totale_inleg, winst = bereken_saldo(
    eenmalige_inleg=1000,
    maandelijkse_inleg=100,
    looptijd=1,
    winst_percentage=5,
    )

    assert round(totale_inleg, 2) == 2200
    assert round(saldo, 2) == 2310
    assert round(winst, 2) == 110

def test_meerdere_jaren():
    saldo, totale_inleg, winst = bereken_saldo(
        eenmalige_inleg=1000,
        maandelijkse_inleg=100,
        looptijd=10,
        winst_percentage=5,
    )

    assert round(totale_inleg, 2) == 13000
    assert round(saldo, 2) == 17477.04
    assert round(winst, 2) == 4477.04
