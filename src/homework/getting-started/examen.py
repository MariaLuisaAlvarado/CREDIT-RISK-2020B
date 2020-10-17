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
def greeting(self):
    return "I'm Prof. {professor_last_name} and {lecture_details}.".format(
        professor_last_name=self.last_name,
        lecture_details=f"I am teaching a lecture named '{self.lecture}'"
            if self.lecture else "I am currently not teaching any lecture")