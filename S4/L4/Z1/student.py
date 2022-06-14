import pupil
import pupil_exception

class Student(pupil.Pupil):

	def __init__(self, given_name: str, given_surname: str):
		super().__init__(given_name, given_surname)
		self._weighs = {}
	
	@property
	def weighs(self):
		return _weighs
		
	def complete_weighs(self, subject: str, weigh):
		if weigh>0 and weigh<=1:
			self._weighs[subject] = weigh
		else:
			raise pupil_exception.IncorrectWeigh

	def mean(self):
		subjects = super().marks.items()
		subweighs = self._weighs.items()
		sum = 0
		for subject, mark in subjects:
			for subjects, weighs in subweighs:
				if(subject==subjects):
					mark *= weighs
			sum += mark
		return sum/len(self._weighs)

	def __str__(self):
		return f"{self._name} {self._surname}: {self.mean()}"