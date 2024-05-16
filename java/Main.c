int main(){
    int x =10, y=12;
    x = x++ + y++;
    printf("%d",x);
    int z = x++;
    printf("\n%d",z);
    return 0;
}