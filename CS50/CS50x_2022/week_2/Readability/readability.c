#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string);
int count_words(string);
int count_sentences(string);

float l;
float w;
float s;

int main(void)
{
    // Ask user for string, store in txt.
    string txt = get_string("Enter your text: ");

    int i = strlen(txt);

    // Convert letters and sentences to avg / 100 w.
    float L = 100 * (l / w);
    float S = 100 * (s / w);

    // Calc coleman-liau index
    int clindex = round(0.0588 * L - 0.296 * S -15.8);

    // Printf "Grade X" if X > 16, printf "Grade 16+".
    if (clindex < 1)
    {
        printf("Grade < 1\n");
    }
    else if (clindex > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", clindex);
    }

}

int count_letters(string txt)
{
    // Count letters
    l = 0;
    for (int i = 0, n = strlen(txt); i < n; i++)
    {
        // If the txt is between a-z (97 - 122) or A-Z (65 - 90), increase letter count.
        if ((txt[i] >= '97' && txt[i] <= '122') || (txt[i] >= '65' && txt[i] <= '90'))
        {
            l++;
        }
    }
    return l;
}

int count_words(string txt)
{
    // Count words
    w = 1;
    for (int i = 0, n = strlen(txt); i < n; i++)
    {
        // If there is a space (ascii 32), then increase word count.
        if (txt[i] == 32)
        {
            w++;
        }
    }
    return w;
}

int count_sentences(string txt)
{
    // Count sentences
    s = 0;
    for (int i = 0, n strlen(txt); i < n; i++)
    {
        // If txt is . (period 46), ! (exclamation 33), or ? (question 63), inscrease sentence count.
        if (txt[i] == 46 || txt[i] == 33 || txt[i] == 63)
        {
            s++;
        }
    }
    return s;
}