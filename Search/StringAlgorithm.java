public class StringAlgorithm {
	public static void main(String[] args) {
		String str = "abcdabcdfgab";
		String sStr = "ab";

		int orStrLen = str.length(); // Original string
		int sStrLen = sStr.length(); // word to find

		char[] searchString= sStr.toCharArray(); // 찾을 단어를 character형 배열로 변환
		char[] allString = str.toCharArray(); // 전체 문장을 character형 배열로 변환

		int start; // 전체 문장에서 찾으려는 단어를 빼 시작 인덱스 구하기
		int i;

		int count = 0; // 문장에서 찾으려는 개수

		for(start=0; start < orStrLen ; start++) { // 전체 문장의 처음부터 시작
			for( i=0; i<sStrLen; i++ ) { // 찾으려는 단어 대입
				if( allString[start] == searchString[i] ) { // 각 단어의 첫번째 단어 비교
					if( allString[start+1] == searchString[I + 1] ) {// 두 번째 단어 비교
						count++; // 두 개 단어 같으면 하나 증가
						}
					}
					else {
						break;
					}
				}
			}
		System.out.println("The number of words found = " + count);
	}
}
