import datetime
import factory
from usermanagement.models import UserActivity


class UserActivityFactory(factory.Factory):
    class Meta:
        model = UserActivity

    username = factory.Sequence(lambda n: "user%d" % n)
    last_login = datetime.date.today()
    login_count = factory.Sequence(lambda n: "%d" % n)
    project_count = factory.Sequence(lambda n: "%d" % n)
