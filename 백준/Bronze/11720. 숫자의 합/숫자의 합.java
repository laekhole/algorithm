import java.util.Scanner;

public class Main {

	
	public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
	int sum=0;
	int N = sc.nextInt();
	sc.nextLine();
	
	String M=sc.nextLine();
	
//	System.out.println(M.length()); 
	int ans[]= new int[M.length()];
	String[] ans2=M.split("");
//	System.out.println(ans2);
	
	for(int i=0;i<M.length();i++) {
		sum+=Integer.parseInt(ans2[i]);
		
	}
	System.out.println(sum);
	
//	char a, b;
//	String str;
//	str = sc.nextLine();
//	a = str.charAt(0);
//	b = str.charAt(2);
//	System.out.println(a+" "+b);
//	sc.close();
//	int A[]=
	}
}