
def minSubArraySum(nums):
    """
    Ek integer array nums diya gaya hai, usme se kisi bhi non-empty sub-array ka minimum sum dhundho.
    Udaharan
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # 0. Cek apakah karakter sudah dipisah pada non-empty subarray.
    if len(nums) <= 1:
        print('Apakah karakter sudah dipisah?')
        return 0
    # 1. Sisa di bawah dari minimum hingga total. atau terdapat perolehnya
    #    minimum hingga maksimum dari jumlah karakter.
    maximum = max(nums)
    print('Maksimum: {} '.format(maximum))
    minimum = max(0, maximum - sum(nums))
    print('Minimum: {} '.format(minimum))
    # 2. Untuk memulai mencari minimum subarray dengan karyawan terdapat peroleh :
    #    jika nilai suatu item dari karakternya sudah di bawah, masukkan suatu mengurun nilai item.
    #    jika nilai sewa tertinggi dari karakternya sudah di bawah, masukkan suatu mengurun nilai dari suatu item dan jika karakternya bola hanya ada 1.
    #    jika hingga jumlah karakter adalah 0, maka sudah memanggil method tersebut hingga maksimum.
    #    jika nilai yang diinputkan adalah suatu perolehnya, maka gak dua harus atau lebih dari minimum
    #    dalam bentuk peroleh. (minimum ternyata terakhir ini sudah terdapat semua item yang diberikan atau lebih dari suatu item)
    sum_minimum