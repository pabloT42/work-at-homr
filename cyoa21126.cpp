#include <iostream>
#include <vector>
#include <string>
using namespace std;

// ------------------------------------------------------------
// STORY PAGE
// ------------------------------------------------------------
class StoryPage
{
public:
	int id;
	string text;
	vector<int> nextPages;        // where you can go
	vector<string> choiceText;    // what the choices say
	bool ending;

	//constructor sets the three main variables
	StoryPage(int newId, string newText, bool isEnd) {
		id = newId;
		text = newText;
		ending = isEnd;
	}

	bool isValidChoice(int choice) {
		//in python this whole loop would be "if choice in nextPages:"
		for (int i = 0; i < (int)nextPages.size(); i++) {
			if (nextPages[i] == choice)
				return true;
		}
		return false;
	}

	void show() {
		cout << "\n----------------------------------------" << endl;
		cout << "Page " << id << endl;
		cout << "----------------------------------------" << endl;
		cout << text << endl;

		if (!ending) {
			cout << endl;
			for (int i = 0; i < nextPages.size(); i++) {
				cout << "- " << choiceText[i] //print out choices
					<< " (Turn to page " << nextPages[i] << ")" << endl; //and their pages
			}
		}
	}
};//end class definition

// ------------------------------------------------------------
// MAIN
// ------------------------------------------------------------
int main()
{
	//game variables////////////////////////////////////////////////////
	vector<StoryPage*> pages;
	int page = 1;
	int choice = 0;

	cout << "========================================" << endl;
	cout << "      THE MOLE MONSTER                  " << endl;
	cout << "      (Type the page number to turn)    " << endl;
	cout << "========================================" << endl;

	///////////////////////////////////////////////////////////////////
	//create pages

	StoryPage* p1 = new StoryPage(1,
		"You are a civil engineer. You dig a hole to inspect the dirt.\n"
		"You climb down into the hole.\n"
		"A giant MOLE MONSTER charges at you!", false);
	p1->nextPages = { 30, 15 };
	p1->choiceText = {
		"To run away",
		"To talk to the mole monster"
	};
	pages.push_back(p1);

	StoryPage* p15 = new StoryPage(15,
		"You try to talk.\n"
		"The mole monster eats you.\n\nTHE END.", true);
	pages.push_back(p15);

	StoryPage* p30 = new StoryPage(30,
		"You climb out of the hole.\n"
		"Nearby is a shed and an excavator.", false);
	p30->nextPages = { 88, 5 };
	p30->choiceText = {
		"To go into the excavator",
		"To hide in the shed"
	};
	pages.push_back(p30);

	StoryPage* p5 = new StoryPage(5,
		"The mole monster can't find you and loses interest.\n"
		"You decide to major in computer science- engineering is too dangerous.\n\nTHE END.", true);
	pages.push_back(p5);

	StoryPage* p88 = new StoryPage(88,
		"The excavator was coded in PYTHON and goes haywire (someone didn't indent correctly).\n"
		"It spins around until you are dizzy, then ejects you into the mole monster's mouth.\n", false);
	p88->nextPages = { 41, 67 };
	p88->choiceText = {
		"venture the moles stomach",
		"climb out its mouth"
	};
	pages.push_back(p88);


	StoryPage* p41 = new StoryPage(41,
		"The mole monster is 'coded' in javascript.\n"
		"the mole disentegrates because javascript isnt a real language.\n\nTHE END.", true);
	pages.push_back(p41);


	StoryPage* p67 = new StoryPage(67,
		"you climbed out of its mouth but now what do you do?!?!?.\n"
		"its coded in c plus plus so its a mighty foe what will you do?.\n", false);
	p67->nextPages = { 17, 38 };
	p67->choiceText = {
		"fight Dr.Mole",
		"Go into a hole dug by Dr.Mole"
	};
	pages.push_back(p67);

	StoryPage* p17 = new StoryPage(17,
		"you square up with doctor mole.\n"
		"do you kick or punch.\n", false);
	p17->nextPages = { 7, 68 };
	p17->choiceText = {
		"kick",
		"punch"
	};
	pages.push_back(p17);

	StoryPage* p7 = new StoryPage(7,
		"you decided to punch Dr.Mole.\n"
		"doctor mole punches you out of the hole and now you major in comp sci.\n", true);
	pages.push_back(p7);

	StoryPage* p68 = new StoryPage(68,
		"you square up with doctor mole.\n"
		"you kicked doctor mole and it digs a hole to run away.\n", false);
	p68->nextPages = { 27, 78 };
	p68->choiceText = {
		"leave the hole",
		"follow the mole hole"
	};
	pages.push_back(p68);

	StoryPage* p38 = new StoryPage(38,
		"you went in to the hole.\n"
		"its a kingdom down here its too late turn back now.\n", false);
	p38->nextPages = { 57, 98 };
	p38->choiceText = {
		"go to a mole bowl shop",
		"Go to the monstrous mole palace"
	};
	pages.push_back(p38);

	StoryPage* p57 = new StoryPage(57,
		"you went in to the mole bowl shop.\n"
		"mole bowls of insect soup fill the air what will you order?\n", false);
	p57->nextPages = { 44, 22 };
	p57->choiceText = {
		"earthworm and beetle mole bowl",
		"ant and snail mole bowl"
	};
	pages.push_back(p57);

	StoryPage* p44 = new StoryPage(44,
		"you HATED the earthworm and beetle bowl.\n"
		"you get sentenced to code in javascript for your opinion.\n", true);
	pages.push_back(p44);

	StoryPage* p22 = new StoryPage(22,
		"you LOVED the ant and snail mole bowl.\n"
		"you become a food reviewer on moletok and become a moleionare.\n", true);
	pages.push_back(p22);

	StoryPage* p38 = new StoryPage(38,
		"you went in to the hole.\n"
		"its a kingdom down here its too late turn back now.\n", false);
	p38->nextPages = { 57, 98 };
	p38->choiceText = {
		"go to a mole bowl shop",
		"Go to the monstrous mole palace"
	};
	pages.push_back(p38);


	///////////////////////////////////////////////////////////////////
	//game loop

	while (page != 0)
	{
		StoryPage* current = NULL; //keeps track of what page we're on

		for (int i = 0; i < pages.size(); i++) {
			if (pages[i]->id == page) //find the page object based on what the id is
				current = pages[i];
		}

		if (current == NULL) {
			page = 1;
			continue;
		}

		current->show(); //display the text

		if (current->ending) {
			page = 0;
			break; //kill loop if done
		}

		cout << "> ";
		cin >> choice;

		if (current->isValidChoice(choice)) //check if page exists
			page = choice; //move to that page
		else
			cout << "That page doesn't exist here." << endl;
	}

	///////////////////////////////////////////////////////////////////
	//clean up memory ('cause we're not lazy python coders anymore...)

	for (int i = 0; i < (int)pages.size(); i++) {
		delete pages[i];
	}

	cout << "\nGame Over. Thanks for playing!" << endl;
	return 0;
}
