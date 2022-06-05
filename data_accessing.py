from GUI_steg_part2 import the_path
from GUI_steg_part2 import embed, extract

msg_flag = False






def do_embedding(final_msg, final_pic_path):
    final_msg = str(final_msg)

    final_pic_path = str(final_pic_path[0])

    final_pic_path.replace('\\\\', "\\")

    f = open(final_pic_path, 'a')

    f.write('\n-\n--\n---\n')
    f.write(final_msg)

    f.close()





def do_extracting(final_pic_path):
    final_pic_path = str(final_pic_path[0])

    final_pic_path.replace('\\\\', "\\")

    f = open(final_pic_path, 'rb')

    bank = f.readlines()
    bank.reverse()

    msg_out = bank[0]  # still a byte here
    msg_out = str(msg_out)

    msg_out = msg_out[2:len(msg_out) - 1]  # getting rid of parenthesis and the b symbol

    return msg_out










if( embed[0]==True and extract[0]==False ):
    from GUI_steg_part2 import the_msg
    do_embedding(the_msg, the_path)
else:
    msg_flag = True
    extracted_message = do_extracting(the_path)

