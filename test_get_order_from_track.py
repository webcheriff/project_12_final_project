import data
import sender_stand_request


#   Successful assertion of getting an order from its track
def assertion_code_200():
	response_pno = sender_stand_request.post_new_order(data.order_body)
	track = response_pno.json()["track"]
	response_goft = sender_stand_request.get_order_from_track(track)
	assert response_goft.status_code == 200


#   Automated assertion of getting an order from its track
def test_get_order_from_track_code_200():
	assertion_code_200()