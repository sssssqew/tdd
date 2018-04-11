/*global $, test, equal */
		$('input').on('keypress', function(){
			$('.has-error').hide();
		});

		test("키 입력 시에 에러가 숨겨져야 한다", function(){
			$('input').trigger('keypress');
			equal($('.has-error').is(':visible'), false);
		});

		test("키 입력이 없으면 에러가 숨겨지지 않는다", function(){
			equal($('.has-error').is(':visible'), true);
		})