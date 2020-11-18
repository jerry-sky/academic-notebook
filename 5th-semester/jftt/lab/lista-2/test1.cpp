#include<iostream>

/** Maly przyklad programu
 *
 *  // autor Maciej Gebala
 *
 */


// /*
using namespace std;
// */

//! Komentarz dokumentacyjny\
	   //i jego // ciag dalszy\
  /* i dalszy */
int some_function(int a) {
	return a << (1 << 4);
}

/*! Nieco inny komentarz dokumentacyjny

	// Komentarz w komentarzu


   */
int main()
{
  /// Komentarz dokumentacyjny \
  ciag dalszy jednolinijkowego komentarza
  int i = 5;
  // Komentarz jednolinijkowy\
  i jego ciÄg dalszy\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
  i dalszy */
  cout << "Jakis program" << endl; // ;
  // A tutaj taki komentarz \
  cout << "Poczatek komentarza /*" << endl; // ala


  /*
	Taki sobie komentarz
	/** z komentarzem w srodku */
  //! i jeszcze inny komentarz \*/
  cout << "Koniec komentarza */ "<< endl; // kot
  cout << "Komentarz /* ala */" << endl;
  /*! I jeszcze jeden
					**/
  // i jeszcze jeden */
  cout << "Komentarz // kot " << endl;
  cout << "Zabawa \" // ala i kot " << endl;
  cout << "Pulapka \" \
           // ma \
           /* ma */ \
           " << endl;
 cout << /*Proba*/"Zabawa \" // ala i kot " << endl;
 printf("Zabawa \" // ala i kot ");
}
