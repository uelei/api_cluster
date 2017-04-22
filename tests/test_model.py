from back.models import ClusterLogs


def test_post_model(session):
    post = ClusterLogs(DeviceID="1")

    session.add(post)
    session.commit()

    assert post.id > 0