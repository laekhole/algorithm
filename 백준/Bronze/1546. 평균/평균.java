import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {

	int n;
	
	Scanner sc = new Scanner(System.in);
	
	n=sc.nextInt();
//	System.out.println(n);
//	sc.nextLine();
	
	int m[] = new int[n];
	int max=0;
	double sum=0;
	
	for (int i=0; i<n; i++) {
		m[i]=sc.nextInt();
		if (max<=m[i]) {
			max=m[i];
		}
//		System.out.println(m[i]);
//		System.out.println(max);

	}

	double m2[]= new double[n];
	for (int i=0; i<n; i++) {
		m2[i]=(double)m[i]*100/max;
		sum+=m2[i];
//		System.out.println(m2[i]);
//		System.out.println(sum);
		

	}
	

//	변수명.getClass().getName()
	System.out.println(((double)sum/n));
	
	
	}
	
}
