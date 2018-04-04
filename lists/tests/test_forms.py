from django.test import TestCase 
from lists.forms import EMPTY_LIST_ERROR, ItemForm 

class ItemFormTest(TestCase):

	def test_form_renders_text_input(self):
		form = ItemForm()
		self.assertIn('placeholder="작업 아이템 입력"', form.as_p())
		self.assertIn('class="form-control input-lg"', form.as_p())

	def test_form_validation_for_blank_items(self):
		form = ItemForm(data={'text':''})
		self.assertFalse(form.is_valid())
		self.assertEqual(
			form.errors['text'],
			[EMPTY_LIST_ERROR]
		)