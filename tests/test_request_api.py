
def test_get_cluster_info(client, session):
    response = client.get("/upload")
    assert response.status_code == 200
    assert response.json == {}


def test_add_cluster_log(client, session):

    post_data = """Device: ID=1; Fw=16071801; Evt=1; Alarms: CoilRevesed=OFF; Power: Active=1832W; Reactive=279var; Appearent=403VA; Line: Current=7.50400019; Voltage=230.08V; Phase=-43,841rad; Peaks: 14.3940001;14.420999499999999;14.46;14.505999599999999;14.1499996;13.925999599999999;13.397999800000003;13.0539999;13.020999900000001;13.074000400000001; FFT Re: 10263;13;145;-13;943;-19;798;0;237; FFT Img: 1465;6;-818;13;1115;6;706;19;699; UTC Time: 2016-10-4 16:47:50; hz: 49.87; WiFi Strength: -62; Dummy: 20"""

    response = client.post("/upload", data=post_data)

    assert response.status_code == 200
    assert "id" in response.json

def test_empty_request_cluster_log(client, session):

    post_data = ""

    response = client.post("/upload", data=post_data)

    assert response.status_code == 400
