1|John Doe|Billing Issue|Billing|123 Elm St|98765-43210|active
2|Jane Smith|Service Delay|Service|456 Oak Ave|87654-32109|inactive
3|Amit Singh|Connection Problem|Technical|789 Pine Rd|76543-21098|active
4|Pooja Mehta|Feedback|General|Block A|65432-10987|active
5|Rahul Verma|Wrong Billing|Billing|Lane 3|54321-09876|inactive
6|Neha Agarwal|Service Interruption|Service|Road 4|43210-98765|active
7|Vikram Joshi|Faulty Meter|Technical|Area 2|32109-87654|inactive
8|Anita Yadav|New Connection|Service|Locality 7|21098-76543|active
9|Deepak Jain|High Bill Amount|Billing|Zone 3|10987-65432|active
10|Kiran Rathi|Service Request|General|Region 8|09876-54321|inactive

awk 'BEGIN{FS="|", count=0} 
{
    if($NF=="active"){
        count = count + 1;
    }
} 
END{print "total active complains are: ",count}' complaint.txt

# -----------------------------------------
1101132490784|Jane Smith|87654-32109|456 Oak Ave|2000.50|Debit Card
1101132490785|Amit Singh|76543-21098|789 Pine Rd|1750.25|Net Banking
1101132490786|Pooja Mehta|65432-10987|Block A|1000.00|Cash
1101132490783|John Doe|98765-43210|123 Elm St|1500.75|Credit Card
1101132490787|Rahul Verma|54321-09876|Lane 3|1200.50|UPI
1101132490788|Neha Agarwal|43210-98765|Road 4|950.75|Credit Card

awk '
BEGIN{FS="|"; cid=1101132490783; yes=0}
{
    if($1==cid){
        print $1"|"$2"|"$5"|"$6;
        yes=1;
    }
}
END{if(yes==0){print "Consumer not found"}}' bill.txt

ALT...

awk -F'|' '$1==1101132490783 {print $1"|"$2"|"$5"|"$6; found=1 } END{if(!found) print "Consumer not found"}' bill.txt 

# -------------------------------------------------
1101132490783|John Doe|1500.75|1600.50|1700.25|1550.00|1800.00
1101132490784|Jane Smith|2000.00|2100.25|1900.50|2200.00|1950.75
1101132490785|Amit Singh|1750.00|1800.75|1700.00|1650.50|1600.00
1101132490786|Pooja Mehta|1000.50|1100.00|950.75|1200.00|1150.25
1101132490787|Rahul Verma|1200.00|1300.50|1250.75|1400.00|1350.00

awk 'BEGIN{FS="|";} {avg=($3+$4+$5+$6+$7)/5; print $1"|"$2"|"avg} END{}' month.txt