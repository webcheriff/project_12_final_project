# Rostislav Cherepanov, 8th cohort — Final project. Test Engineer Plus
import test_get_order_from_track
import data

result = test_get_order_from_track.test_get_order_from_track_code_200()


def result_of_api_automation(a, b):
	if a == b:
		print("Successful test")
	else:
		print("Test failed")


result_of_api_automation(result, data.status_code_successful)
