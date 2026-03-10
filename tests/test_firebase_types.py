"""Unit tests for strict Firebase schema models."""

from huckleberry_api.firebase_types import (
    FirebaseGrowthData,
    FirebaseDiaperDocumentData,
    FirebaseFeedDocumentData,
    FirebaseSleepDocumentData,
)


def test_feed_document_accepts_empty_last_summary_maps() -> None:
    """Empty feed summary maps should validate after history is cleared."""
    model = FirebaseFeedDocumentData.model_validate(
        {
            "prefs": {
                "lastBottle": {},
                "lastNursing": {},
                "lastSolid": {},
            }
        }
    )

    assert model.prefs is not None
    assert model.prefs.lastBottle is not None
    assert model.prefs.lastBottle.mode is None
    assert model.prefs.lastBottle.bottleType is None
    assert model.prefs.lastNursing is not None
    assert model.prefs.lastNursing.mode is None
    assert model.prefs.lastNursing.duration is None
    assert model.prefs.lastSolid is not None
    assert model.prefs.lastSolid.mode is None
    assert model.prefs.lastSolid.foods is None


def test_sleep_and_diaper_documents_accept_empty_last_summary_maps() -> None:
    """Empty sleep and diaper summary maps should validate after deletions."""
    sleep_model = FirebaseSleepDocumentData.model_validate({"prefs": {"lastSleep": {}}})
    assert sleep_model.prefs is not None
    assert sleep_model.prefs.lastSleep is not None
    assert sleep_model.prefs.lastSleep.start is None
    assert sleep_model.prefs.lastSleep.duration is None

    diaper_model = FirebaseDiaperDocumentData.model_validate(
        {
            "prefs": {
                "lastDiaper": {},
                "lastPotty": {},
            }
        }
    )
    assert diaper_model.prefs is not None
    assert diaper_model.prefs.lastDiaper is not None
    assert diaper_model.prefs.lastDiaper.mode is None
    assert diaper_model.prefs.lastDiaper.start is None
    assert diaper_model.prefs.lastPotty is not None
    assert diaper_model.prefs.lastPotty.mode is None


def test_growth_model_accepts_live_app_imperial_summary_units() -> None:
    """Growth schema should accept the composite imperial units emitted by the live app."""
    model = FirebaseGrowthData.model_validate(
        {
            "_id": "1773175568582-ef0c64260d2686001e96",
            "head": 10.2,
            "headUnits": "hin",
            "height": 5.333333333333333,
            "heightUnits": "ft.in",
            "lastUpdated": 1773175568.582,
            "mode": "growth",
            "multientry_key": None,
            "offset": -120.0,
            "start": 1773175490.0,
            "type": "health",
            "weight": 14.125,
            "weightUnits": "lbs.oz",
        }
    )

    assert model.weightUnits == "lbs.oz"
    assert model.heightUnits == "ft.in"
    assert model.headUnits == "hin"


def test_growth_model_accepts_sparse_live_app_data_rows() -> None:
    """Growth data rows from the live app can omit summary-only fields like `_id` and `type`."""
    model = FirebaseGrowthData.model_validate(
        {
            "head": 30.9,
            "headUnits": "hcm",
            "height": 162.0,
            "heightUnits": "cm",
            "lastUpdated": 1773175665.799,
            "mode": "growth",
            "offset": -120.0,
            "start": 1773175645.668,
            "weight": 9.41,
            "weightUnits": "kg",
        }
    )

    assert model.id_ is None
    assert model.type is None
    assert model.isNight is None
    assert model.weightUnits == "kg"
    assert model.heightUnits == "cm"
