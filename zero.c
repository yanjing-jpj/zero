#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <conio.h>
#include <string.h>
//int n=300;//��Ʒ����
//double c;//��������
//int v[300];//������Ʒ�ļ�ֵ
//int w[300];//������Ʒ������
//double cw = 0.0;//��ǰ��������
//double cp = 0.0;//��ǰ��������Ʒ��ֵ
//double bestp = 0.0;//��ǰ���ż�ֵ
//double perp[100];//��λ��Ʒ��ֵ�����
//int order[100];//��Ʒ���
//int put[100];//�����Ƿ�װ��
/*
//����λ��ֵ����
void knapsack()
{
    int i,j;
    int temporder = 0;
    double temp = 0.0;

    for(i=1;i<=n;i++)
        perp[i]=v[i]/w[i];
    for(i=1;i<=n-1;i++)
    {
        for(j=i+1;j<=n;j++)
            if(perp[i]<perp[j])//ð������perp[],order[],sortv[],sortw[]
        {
            temp = perp[i];
            perp[i]=perp[i];
            perp[j]=temp;

            temporder=order[i];
            order[i]=order[j];
            order[j]=temporder;

            temp = v[i];
            v[i]=v[j];
            v[j]=temp;

            temp=w[i];
            w[i]=w[j];
            w[j]=temp;
        }
    }
}
*/
int max(int a,int b)
{
    if(a>b)
        return a;
    else
        return b;
}
//��̬�滮�㷨
int Knapsack(int v[],int w[],int n,int C,int x[])
{
    int V[n+1][C+1];
    int i,j;
    for(i=0;i<=n;i++)
        V[i][0]=0;
    for(j=0;j<=C;j++)
        V[0][j]=0;
    for(i=1;i<=n;i++)
        for(j=1;j<=C;j++)
            if(j<w[i])
                V[i][j] = V[i-1][j];
            else
                V[i][j] = max(V[i-1][j],V[i-1][j-w[i]]+v[i]);
    for(j=C,i=n;i>0;i--)
    {
        if(V[i][j]>V[i-1][j])
        {
            x[i]=1;
            j=j-w[i];
        }
        else
            x[i]=0;
    }
    return V[n][C];
}
//���������ļ�ֵ:�����Ƚ��зǵ�������
void three(int v[],int w[],int n)
{
    //int temporder = 0;
    int index=0;
    int vv[n],ww[n];
    float temp = 0.0,perp[n];
    for(int i=0;i<n;i++)
        if((i+1)%3==0)
        {
            perp[index]=(float)(v[i])/w[i];
            vv[index]=v[i];
            ww[index]=w[i];
            index++;
           // printf("-+-%f\n",perp[index-1]);
        }
    for(int i=0;i<index;i++)
        for(int j=i+1;j<index;j++)
            if(perp[i]<perp[j])//ð������perp[],order[],sortv[],sortw[]
            {
                temp = perp[i];
                perp[i]=perp[j];
                perp[j]=temp;
/*
                temporder=order[i];
                order[i]=order[j];
                order[j]=temporder;
*/
                temp = vv[i];
                vv[i]=vv[j];
                vv[j]=temp;

                temp=ww[i];
                ww[i]=ww[j];
                ww[j]=temp;

            }
    for(int i=0;i<index;i++)
    {
        printf("��ֵ-�����ȣ�%f      ��ֵ��%d       ������%d\n",perp[i],vv[i],ww[i]);
    }
}
/*
//���ݺ���
void backtrack(int i)
{
    double bound(int i);
    if(i>n)
    {
        bestp = cp;
        return;
    }
    if(cw+w[i]<=c)
    {
        cw+=w[i];
        cp+=v[i];
        put[i]=1;
        backtrack(i+1);
        cw-=w[i];
        cp-=v[i];
    }
    if(bound(i+1)>bestp)//������������������
        backtrack(i+1);
}

//�����Ͻ纯��
double bound(int i)
{
    double leftw= c-cw;
    double b = cp;
    while(i<=n&&w[i]<=leftw)
    {
        leftw-=w[i];
        b+=v[i];
        i++;
    }
    if(i<=n)
        b+=v[i]/w[i]*leftw;
    return b;

}
*/
void char_to_number(char date[],int N,int number[])     //N:���ֵĸ���
{
    int i=0;
    int length = strlen(date);
    int index1=0,index2=0,index_str=0;
    char apart,str[4];
   // printf("--%d",length);
    while(index2<length)
    {
        if(date[index2]==',')
        {
            while(index1<index2)
            {
                str[index_str++] = date[index1++];
                //index1++;
            }
            int temp=0,power;
            power=index_str-1;
            for(int j=0;j<index_str;j++)
            {
                int n = str[j]-'0';
                temp = temp+n*pow(10,power);
                power--;
 //               printf("str=%c,j=%d,,++%d,--%d\n",str[j],j,temp,n);
            }
                //printf("%c",str[j]);

            index_str=0;
            number[i++]=temp;
   //         printf("))%d\n",number[i-1]);
            index1 = index2+1;
        }
        index2++;
    }
}
int main()
{
    int n,C,M=1500;
    char date1[M],date2[M];
	char string[M];
	clock_t start,finish;
	start=clock();
	//��ȡ��ֵ
	printf("��Ʒ��ֵ:\n");
	FILE *fp = fopen("C:/Users/Acer/Desktop/test1.txt","r");
	while( fgets(string, sizeof(string), fp) != NULL )//���ж�ȡ����
	{
		strcpy(date1,string);
		printf("%s\n",date1);
	}
	fclose(fp);

	//��ȡ����
	printf("��Ʒ����:\n");
	FILE *fp2 = fopen("C:/Users/Acer/Desktop/test2.txt","r");
	while( fgets(string, sizeof(string), fp) != NULL )//���ж�ȡ����
	{
		strcpy(date2,string);
		//*r = strtok(date,apart);
		printf("%s\n",date2);
	}
	fclose(fp2);
	printf("��������Ʒ��������������");
    scanf("%d%d",&n,&C);
    int v[n],w[n];
	//printf("%c",date2[1]);
    char_to_number(date1,300,v);
    //printf("_____\n\n\n");
    char_to_number(date2,300,w);


    int x[n];
    for(int i=0;i<n;i++)
    {
        x[i]=0;
    }
    int maxV=Knapsack(v,w,n,C,x);
    //backtrack(1);
    printf("���м�ֵΪ��%d\n",maxV);
    printf("��Ҫװ�����Ʒ����ǣ�");
    for(int i=0;i<n;i++)
    {
        if(x[i]==1)
            printf("%d ",i+1);
    }
    finish=clock();
    printf("\n����ʱ��: %f",(double)(finish - start) / CLK_TCK);
    printf("\n����ֵ�������ıȣ��ǵ�������:\n");
    three(v,w,n);
    return 0;
}
