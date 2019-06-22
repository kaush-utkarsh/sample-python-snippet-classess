
try:
    f = open('curruptfile.txt')
    # if f.name == 'currupt_file.txt':
    #     raise Exception
except IOError as e:
    print('First!')
except Exception as e:
    print('Second')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

print('End of program')


# import sys, traceback

# def run_user_code(envdir):
#     source = raw_input(">>> ")
#     try:
#         exec source in envdir
#     except:
#         print "Exception in user code:"
#         print '-'*60
#         traceback.print_exc(file=sys.stdout)
#         print '-'*60

# envdir = {}
# while 1:
#     run_user_code(envdir)