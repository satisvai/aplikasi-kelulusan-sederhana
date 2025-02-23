#include <iostream>
#include <string>

using namespace std;

int main() {
    // Deklarasi variabel
    string nama, nim, prodi, kelas;
    double nilai_absen, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir;
    char nilai_huruf;
    string status_kelulusan;

    // Input data mahasiswa
    cout << "Masukkan nama mahasiswa: ";
    getline(cin, nama);
    cout << "Masukkan NIM: ";
    cin >> nim;
    cout << "Masukkan Program Studi: ";
    cin.ignore(); // Mengabaikan newline sebelum getline
    getline(cin, prodi);
    cout << "Masukkan Kelas: ";
    getline(cin, kelas);
    cout << "Masukkan nilai absen: ";
    cin >> nilai_absen;
    cout << "Masukkan nilai tugas: ";
    cin >> nilai_tugas;
    cout << "Masukkan nilai UTS: ";
    cin >> nilai_uts;
    cout << "Masukkan nilai UAS: ";
    cin >> nilai_uas;

    // Menghitung nilai akhir
    nilai_akhir = (0.1 * nilai_absen) + (0.2 * nilai_tugas) + (0.3 * nilai_uts) + (0.4 * nilai_uas);

    // Menentukan nilai huruf
    if (nilai_akhir >= 80) {
        nilai_huruf = 'A';
    } else if (nilai_akhir >= 70) {
        nilai_huruf = 'B';
    } else if (nilai_akhir >= 55) {
        nilai_huruf = 'C';
    } else if (nilai_akhir >= 40) {
        nilai_huruf = 'D';
    } else {
        nilai_huruf = 'E';
    }

    // Menentukan status kelulusan
    if (nilai_akhir >= 55) {
        status_kelulusan = "LULUS";
    } else {
        status_kelulusan = "TIDAK LULUS";
    }

    // Menampilkan hasil
    cout << "\nHasil Perhitungan Nilai Akhir:\n";
    cout << "Nama: " << nama << endl;
    cout << "NIM: " << nim << endl;
    cout << "Program Studi: " << prodi << endl;
    cout << "Kelas: " << kelas << endl;
    cout << "Nilai Akhir: " << nilai_akhir << endl;
    cout << "Nilai Huruf: " << nilai_huruf << endl;
    cout << "Status Kelulusan: " << status_kelulusan << endl;

    return 0;
}
