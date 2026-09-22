from fastapi.testclient import TestClient

from app import app, activities

client = TestClient(app)


def test_unregistered_participant_is_removed_from_activity():
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    activities[activity_name]["participants"] = [
        participant
        for participant in activities[activity_name]["participants"]
        if participant != email
    ]

    signup_response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )
    assert signup_response.status_code == 200
    assert email in activities[activity_name]["participants"]

    delete_response = client.delete(
        f"/activities/{activity_name}/participants/{email}"
    )
    assert delete_response.status_code == 200
    assert email not in activities[activity_name]["participants"]
