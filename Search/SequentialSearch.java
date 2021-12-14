import java.util.Scanner;

public class SequentialSearch {

	public static void main(String[] args) {
		int[] dataArray = { 4, 21, 2, 10, 11, 16 };

		System.out.println("검색할 데이터 입력: ");
		Scanner scan = new Scanner(System.in);
		int search = Integer.parseInt(scan.nextLine().
		trim()); // 데이터 입력

		int result = sequentialSearch(dataArray, search);

		if(result == -1)
			System.out.println("couldn't find the data");
		else
			System.out.println("The location of the data is " + result);
	}

	public static int sequentialSearch(int[] arr, int search) {
		for (int i = 0; i < arr.length; i++) { // 순서대로 비교하기 위해 배열의 크기만큼 반복
			if (arr[i] == search) // 비교할 데이터가 배열에 있다면 배열의 위치 return, 없다면 -1 return
			return i;
		}
		return -1;
	}
}
