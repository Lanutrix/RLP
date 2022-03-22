from ast import Try
import capture
def main():
    path=input()
    try:        path=int(path)
    except:     pass
    capture.main_fnc(path)
if __name__=="__main__":
    main()