/* This program asks used to convers numbers from one unit to another
1.kms to miles
2.inches to foot
3.cms to inches
4.pounds to kgs
5.inches to meters
 */

#include <stdio.h>
#include <conio.h>
float kmstomiles(float kms)
{
    return (kms * 0.621371);
}
float inchestofoot(float inches)
{
    return (inches * 0.0833333);
}
float cmstoinches(float cms)
{
    return (cms * 0.393701);
}
float poundstokgs(float pounds)
{
    return (pounds * 0.453592);
}
float inchestometers(float inches)
{
    return (inches * 0.0254);
}

int main()
{
    int conv;
    float unit, result;
    char anyKey;

    choose:
    
    while (1)
    {
        start:
        printf("Select the conversion: \n[1.] kms to miles \n[2.] Inches to foot \n[3.] cms to inches \n[4.] pounds to kgs \n[5]. inches to meters \n\n[0]. To quit the program \n ");
        scanf("%d", &conv);
        switch (conv)
        {
        case 0:
            printf("Quiting th program...");
            goto end;
            break;
        case 1:
            printf("You have chosen KMS to MILES\n");
            printf("Enter the number in kms: ");
            scanf("%f", &unit);
            printf("%f kms = %f miles\n", unit, kmstomiles(unit));
            printf("------------------------------------------------------------------\n");
            // printf("Press any key to continue....\n");
            // scanf(" %c", &anyKey);
            // goto start;
            break;
        case 2:
            printf("You have chosen INCHES to FOOT\n");
            printf("Enter the number in inches: ");
            scanf("%f", &unit);
            printf("%f inches = %f foot\n", unit, inchestofoot(unit));
            printf("------------------------------------------------------------------\n");
            break;
        case 3:
            printf("You have chosen CMS to INCHES\n");
            printf("Enter the number in CMS: ");
            scanf("%f", &unit);
            printf("%f cms = %f inches\n", unit, cmstoinches(unit));
            printf("------------------------------------------------------------------\n");
            break;
        case 4:
            printf("You have chosen POUNDS to KGS\n");
            printf("Enter the number in kms: ");
            scanf("%f", &unit);
            printf("%f pounds = %f kgs\n", unit, poundstokgs(unit));
            printf("------------------------------------------------------------------\n");
            break;
        case 5:
            printf("You have chosen INCHES to METERS\n");
            printf("Enter the number in kms: ");
            scanf("%f", &unit);
            printf("%f inches = %f meters\n", unit, inchestometers(unit));
            printf("------------------------------------------------------------------\n");
            break;
        default:
            printf("*** Plese choose from 1 to 5 ***\n");
            goto choose;
            break;
        }
    }
    end:
    getch();
    return 0;
}
