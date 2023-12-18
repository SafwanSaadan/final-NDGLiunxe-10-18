import random
import os

def ask_question(question, options, answers):
    print("="*75)
    print("Cisco: NDG Linux Essentials << Chapter 10-18 Exam Final Modules >>                        |  <.. Eng.Safwan Saadan ..> |")
    print("="*75)
    print(question)
    options_with_indices = list(enumerate(options, start=1))
    random.shuffle(options_with_indices)  # يقوم بترتيب الخيارات بشكل عشوائي مع الفهارس
    correct_options = []
    for index, option in options_with_indices:
        print(f"{index}. {option}")
        if option in answers:
            correct_options.append(index)

    while True:
        try:
            print("")
            user_answer = input("Select the correct options (separated by comma): ")
            user_answer = user_answer.split(",")  # تجزئة الإجابات المدخلة
            user_answer = [int(answer.strip()) for answer in user_answer]  # تحويل القيم من نص إلى عدد صحيح
            break
        except ValueError:
            print("="*75)
            print("Invalid input! Please enter the options as comma-separated numbers.")
            print("="*75)

    if set(user_answer) == set(correct_options):
        print("="*75)
        print("Your answer is correct!")
        print("")
        input("Press Enter to continue...")
        os.system("cls" if os.name == "nt" else "clear")  # مسح الشاشة
        return True
    else:
        print("="*75)
        print(f"Your answer is incorrect! The correct answers are {correct_options}.")
        print("")
        input("Press Enter to continue...")
        os.system("cls" if os.name == "nt" else "clear")  # مسح الشاشة
        return False

def quiz(questions):
    score = 0

    random.shuffle(questions)  # يقوم بترتيب الأسئلة بشكل عشوائي
    for question in questions:
        is_correct = ask_question(question['question'], question['options'], question['answer'])
        if is_correct:
            score += 1

    print("="*75)
    percentage = (score / len(questions)) * 100
    print(f"Your percentage of correct answers is {percentage}%")
    print("="*75)

    repeat = input("Do you want to retake the quiz? (yes/no): ")

    if (repeat.lower() == "yes" or repeat.lower() == "y" or repeat.lower() == "" or repeat.lower() == "1" or repeat.lower() == "t"
         or repeat.lower() == "نعم" or repeat.lower() == "ايوه" or repeat.lower() == "اي" or repeat.lower() == "يب"):
        os.system("cls" if os.name == "nt" else "clear")
        quiz(questions)
    else:
        exit()
# تعريف الأسئلة والخيارات
questions = [
    {
        'question': 'A pipe allows you to…',
        'options': ['…type multiple commands at one prompt.', '…send the output of a command to a file.',
                     '…send the same input to multiple commands.', '…send the output of one command to another.'],
        'answer': '…send the output of one command to another.'
    },
    {
        'question': 'Channel 2 is:',
        'options': ['STDOUT', 'STDERR', 'STDIN', 'STDALL'],
        'answer': 'STDERR'
    },
    {
        'question': 'The grep command…',
        'options': ['…will display the line numbers in a file that contain a specified Regular Expression.',
                    '…will display all the lines in a file containing the specified Regular Expression.',
                    '…will display all the lines that begin with the specified Regular Expression.',
                    '…is not case sensitive.'],
        'answer': '…will display all the lines in a file containing the specified Regular Expression.'
    },
    {
        'question': 'Which command can be used to print line numbers?',
        'options': ['num','nl', 'ln','sort'], 
        'answer': 'nl'
    },
     {
        'question': 'Which of the following commands can be used to scroll through a text file?(choose two)',
        'options': ['more','cat', 'some','less'],
        'answer': ['more','less']
    },
    {
        'question': 'Which are appropriate editors for writing shell scripts?(choose two)',
        'options': ['nano','vi', 'LibreOffice Writer','Firefox','/bin/bash'],
        'answer': ['nano','vi']
    },
    {
        'question': 'Which of the following are correct about for and while loops?(choose two)',
        'options': ['for loops require a variable over which to iterate','for loops have a test each cycle to determine if it should run again',
                     'while loops have a test each cycle to determine if it should run again','for loops operate over a fixed list of items',
                     'while loops operate over a fixed list of items'],
        'answer': ['while loops have a test each cycle to determine if it should run again','for loops operate over a fixed list of items']
    },
    {
        'question': 'What is the correct way to assign the word “Hello” to a variable?',
        'options': ['$A=”Hello”','echo “Hello” &gt; A', 'A=”Hello”','A = “Hello”','echo $A “Hello”'], 
        'answer': 'A=”Hello”'
    },
    {
        'question': 'What is the correct way to save the current directory to a variable?',
        'options': ['pwd $A','pwd | $A', 'A=`pwd`','A=pwd','A=cwd'], 
        'answer': 'A=`pwd`'
    }, 
    {
        'question': 'What is the meaning of $(( $i + 1)) ?',
        'options': ['This runs the command stored in variable i','1 will be added to the i variable',
                     'If i is 0, the loop will stop','This will return the value of the first argument to the script',
                     'This will return the value of the next argument to the script'], 
        'answer': '1 will be added to the i variable'
    }, 
    {
        'question': 'Which of the following are valid CPU types for Intel-based platforms?(choose two)',
        'options': ['24-bit','32-bit','48-bit','64-bit'], 
        'answer': ['32-bit','64-bit']
    }, 
    {
        'question': 'Choose all of the following statements that are true in regard to virtual RAM: (choose three)',
        'options': ['Virtual RAM is stored in the CPU','Virtual RAM is also called swap space',
                    'Virtual RAM is stored on a hard drive','Virtual RAM is used when available physical RAM is low'], 
        'answer': ['Virtual RAM is also called swap space','Virtual RAM is stored on a hard drive',
                   'Virtual RAM is used when available physical RAM is low']
    }, 
    {
        'question': 'A division of a hard drive may be referred to as a _______ ',
        'options': ['label','portion','partition','block'], 
        'answer': 'partition'
    }, 
    {
        'question': 'The fdisk command is a tool used for working with the MBR partitioned disks. True or False?',
        'options': ['True','False'], 
        'answer': 'True'
    }, 
    {
        'question': 'Which of the following commands will display CPU information?(choose two)',
        'options': ['arch','showcpu','lspic','cpuinfo','lscpu'], 
        'answer': ['arch','lscpu']
    }, 
    { 
        'question': 'The Process ID (PID) of the init process is:',
        'options': ['varies','1','100','0'], 
        'answer': '1'
    }, 
    { 
        'question': 'What directory typically contains log files?',
        'options': ['/usr/log','/proc/loc','/var/log','/log'], 
        'answer': '/var/log'
    }, 
    {
        'question': 'The /var directory has files that change over time. True or False?',
        'options': ['True','False'], 
        'answer': 'True'
    }, 
    {
        'question': 'Which of the following commands will allow you to view all processes on the system?(choose two)',
        'options': ['ps -A','ps aux','ps -eLf','ps','ps -ef'], 
        'answer': 'ps aux'
    }, 
    { 
        'question': 'Which directory is the root of the filesystem?',
        'options': ['/','/root','/sys','/home','/var'], 
        'answer': '/'
    }, 
     { 
        'question': 'A service is…',
        'options': ['…a file that contains configuration information','…a feature provided by one computer to another.',
                    '…another name for a computer’s hostname.','…like an IP address'], 
        'answer': '…a feature provided by one computer to another.'
    }, 
     {
        'question': 'Only servers have hostnames. True or False?',
        'options': ['True','False'], 
        'answer': 'False'
    }, 
    {
        'question': 'Which of the following are valid IPv4 addresses?(choose two)',
        'options': ['192.301.25.25','192.105.10.10.2','192.105.10.10','10.33.55.77'], 
        'answer': ['192.105.10.10','10.33.55.77']
    }, 
    { 
        'question': 'Which of the following commands will allow you to log into a remote machine?',
        'options': ['netstat','dig','route','ssh'], 
        'answer': 'ssh'
    },
    {
        'question': 'Which files contain user account information?(choose two)',
        'options': ['/etc/shadow','/etc/passwords','/etc/group','/etc/passwd'], 
        'answer': ['/etc/shadow','/etc/passwd']
    },
    { 
        'question': 'Which command will display the UID, GID and groups your current user belongs to?',
        'options': ['id','Who','about','whoami'], 
        'answer': 'id'
    },
    {
        'question': 'Each user belongs to at least one group. True or False?',
        'options': ['True','False'], 
        'answer': 'True'
    }, 
    { 
        'question': 'Which command will display the users that are currently logged in to the system?',
        'options': ['whoami','about','who','id'], 
        'answer': 'who'
    },
    { 
        'question': 'Which command will display the groups that the root user belongs to?',
        'options': ['groups -a','all -t','all','id root','group -r'],
        'answer': 'id root'
    },
    { 
        'question': 'UIDs 1-499 are usually reserved for what kind of users?',
        'options': ['Are not used for user accounts, but for group accounts',
                    'System accounts, such as server processes','Log-in (human) users','Remote log-in accounts'], 
        'answer': 'System accounts, such as server processes'
    },
    { 
        'question': 'Which of the following options for the useradd command allows root to specify the UID to be associated with the account?',
        'options': ['-g','-M','-u','-G'], 
        'answer': '-u'
    },
    { 
        'question': 'Which command can be used to determine a user’s most recent log in?',
        'options': ['shell','login','last','history'], 
        'answer': 'last'
    },
    { 
        'question': 'Which of the following files contains encrypted user password information?',
        'options': ['/etc/passwd','/etc/usr','/etc/group','/etc/shadow'], 
        'answer': '/etc/shadow'
    },
    { 
        'question': 'Which of the following options for the useradd command allows you to use a different primary group then the default?',
        'options': ['-G','-g','-u','-U'], 
        'answer': '-g'
    },
    { 
        'question': 'Which of the following commands can be used to modify a user?',
        'options': ['useradd','moduser','adduser','usermod'], 
        'answer': 'usermod'
    },
    {
        'question': 'Which of the following are methods for setting permissions using the chmod command?(choose two)',
        'options': ['primary','symbolic','letter','octal'], 
        'answer': ['symbolic','octal']
    },   
    {
        'question': 'The chown command can be used to change the owner and group of a file. True or False?',
        'options': ['True','False'], 
        'answer': 'True'
    }, 
    { 
        'question': 'The chmod command can be used on a file by:',
        'options': ['The file owner','A user that belongs to the files current group',
                    'The file owner and root','Only root'], 
        'answer': 'The file owner and root'
    },
    {
        'question': 'The execute permission is never set on files by default. True or False?',
        'options': ['True','False'], 
        'answer': 'True'
    },
    { 
        'question': 'The sticky bit permission…',
        'options': ['…changes the group ownership of existing files in a directory.',
                    '…prevents others from removing files they don’t own from a common directory.',
                    '…prevents others from overwriting files they don’t own in common directories.',
                    '…sets the group ownership of any new file created in a directory'], 
        'answer': '…prevents others from removing files they don’t own from a common directory.'
    },
    { 
        'question': 'The setuid permission…',
        'options': ['…reports the output of a script to the owner.','…allows a command to be run as the file owner.',
                    '…prevents the owner of a file from being changed.','…allows files in a directory to be manipulated as by the directory owner'], 
        'answer': '…allows a command to be run as the file owner.'
    },
     {
        'question': 'The setgid permission… (choose two)',
        'options': ['…allows a command to be run as the group owner of the file.','…prevents the group owner of a file from being changed.',
                    '…allows files created in a directory to be owned by the group that owns the directory.','…can only be set on files'], 
        'answer': ['…allows a command to be run as the group owner of the file.','…allows files created in a directory to be owned by the group that owns the directory.']
    }, 
    { 
        'question': 'Which of the following ls commands, when executed, will only show information about the directory itself? (choose two)',
        'options': ['ls -h','ls -d','ls -ld','ld -a'], 
        'answer': ['ls -d','ls -ld']
    },

    # يمكنك إضافة المزيد من الأسئلة هنا
]

num_questions = 43
selected_questions = random.sample(questions, k=num_questions)  # يقوم باختيار عدد معين من الأسئلة بشكل عشوائي وبدون تكرار
quiz(selected_questions)

#Eng : Safwan Saadan