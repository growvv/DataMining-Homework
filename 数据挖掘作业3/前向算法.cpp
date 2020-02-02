#include<cstdio>
#include<cstring>
using namespace std;

double A[3][3] = {{0.4, 0, 0}, {0.6, 0.8, 0}, {0, 0.2, 1}};
double B[2][3] = {{0.7, 0.4, 0.8}, {0.3, 0.6, 0.2}};
double alpha[3] = {1, 0, 0};
char list[100];
int t=0;

int main()
{
    printf("«Î ‰»Îπ€≤Ï∑˚∫≈–Ú¡–£∫");
    scanf("%s", list);
    int len = strlen(list);
    for(int i = 0;i < 3;i++)  alpha[i] *= B[list[0]-'A'][i];

    printf("t=%d: ", ++t);
    for(int i = 0;i <3;i++) printf("%.8f ", alpha[i]);
    printf("\n");

    for(int i = 1; i < len;i++)
    {
        double tmpalpha[3];
        for(int i = 0;i <3;i++)  tmpalpha[i] = 0;
        for(int j = 0;j <3;j++)
            for(int k = 0;k < 3;k++)
            {
                tmpalpha[j] += alpha[k]*A[j][k]*B[list[i]-'A'][j];

            }
        for(int i = 0;i < 3;i++)  alpha[i] = tmpalpha[i];

        printf("t=%d: ", t++);
        for(int i = 0;i <3;i++) printf("%.8f ", alpha[i]);
        printf("\n");
    }
    double ans = 0;
    for(int i = 0;i < 3;i++)  ans += alpha[i];
    printf("ans: %.8f\n", ans);
    return 0;
}
