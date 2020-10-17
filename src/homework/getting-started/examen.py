@property
def lecture(self):
    return self._kwargs.get("lecture")


def assign_lecture(self, lecture_name, override=False, fail=True):

    FAIL_MESSAGE = f"Cannot assign lecture {lecture_name} to professor " + \
                    f"{self.full_name} because {self.lecture} was previously assigned. "
    if not self.lecture or override:
        self._kwargs["lecture"] = lecture_name
    elif not fail:
        print(FAIL_MESSAGE)
    else:
        raise ValueError(FAIL_MESSAGE)
