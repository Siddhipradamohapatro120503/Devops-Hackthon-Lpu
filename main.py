import Text_content_gen
# import Url_to_png
import linkdlen_test
import text_getter


promt = text_getter.get_next_line_from_file("IDEA.txt", 0)

output_promt = Text_content_gen.openai_generate(promt)

linkdlen_test.description_input(output_promt)