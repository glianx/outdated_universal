// create and return bitboard face
long int get_bin_face(long int x) {
    long int bin_face = 0;
    // iterate through sticker indices 7 - 0
    for (long int i = 0; i < 8; i++) {
        // add sticker in index 7-i to bitboard face
        // x is left-shifted i * 8 bits = i bytes = i stickers
        bin_face += (x << i * 8);
    }
    return bin_face;
}

// create and return bitboard cube
long int * get_bin_cube() {
    static long int bin_cube[6];
    // iterate through 6 colour faces + 1 blank face
    for (long int x = 0; x < 7; x++) {
        // get bin_face and set xth face of bin_cube as bin_face
        long int bin_face = get_bin_face(x);
        bin_cube[x] = bin_face;

        // convert bin_face decimal to binary
        string binary = bitset<64>(bin_face).to_string();

        // output decimal and binary versions for debugging
        cout << bin_face << endl;
        cout << binary << endl;
    }

    return bin_cube;
}



// return bin_face rotated clockwise
    // 01234567 bin_face bytes indices
    // 67000000 bin_face << 48
    // 00012345 bin_face >> 16
    // -------- OR bitwise operator
    // 67012345 (bin_face << 48) | (bin_face >> 16)
long int get_cw_rot_bin_face(long int bin_face) {
    return (bin_face << 48) | (bin_face >> 16);
}

// return bin_face rotated clockwise
long int get_ccw_rot_bin_face(long int bin_face) {
    return (bin_face << 16) | (bin_face >> 48);
}

// return cube state after U move
long int * get_umove_cube(long int bin_cube[6]) {
    // clockwise rotate up face
    bin_cube[0] = get_cw_rot_bin_face(bin_cube[0]);

    // rotate top row of surrounding faces by swapping
    // set temporary face variable for 4th face
    long int temp_face = (bin_cube[4] & ((1L << 40) - 1)) | (bin_cube[1] & ((1L << 24) - 1) << 40);
    // iterate over faces 1 to 3, inclusive, for swapping
    for (int i = 1; i < 4; i++) {
        // bin_cube[i] & ((1L << 40) - 1) takes the stickers from indices 7 to 3, inclusive (lower 2/3 rows)
        // bin_cube[i+1] & ((1L << 24) - 1) << 40 takes the stickers from indices 0 to 2, inclusive (upper 1/3 row)
        // OR bitwise operation combines these two, and sets top row of bin_cube[i] as top row of counterclockwise face
        bin_cube[i] = (bin_cube[i] & ((1L << 40) - 1)) | (bin_cube[i+1] & ((1L << 24) - 1) << 40);
    }
    // set 4th face as temporary variable to complete rotation
    bin_cube[4] = temp_face;
    return bin_cube;
}



