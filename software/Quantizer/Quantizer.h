/*
 * Quantizer library
 * Rich Holmes
 * 
 * Based on:
 * =======
 * TELEXo Eurorack Module
 * (c) 2016 Brendon Cassidy
 * MIT License
 * =======
 *
 * Mods include:
 * Get rid of frequency stuff, we don't need it. Can always calculate it
 * from Value anyway.
 *
 * Use avr/pgmspace to put scale data in program space, saving
 * dynamic memory.
 *
 */
 
#ifndef Quantizer_h
#define Quantizer_h

#include "Arduino.h"
#include <avr/pgmspace.h>

#define DACTOP 4095   // limit of DAC (2**12-1)
#define DAC1   4095   // DAC counts corresponding to defined voltage
#define V1     5.0    // voltage corresponding to DAC1
#define DACPEROCTAVE  (DAC1/V1)  // DAC counts per octave
#define SCALESET 1    // 0 for common scales, 1 for esoteric scales

struct QuantizeResponse {
  int Note; 
  int Value;
};

/*
 * Quantizes values 0-4095 to various tuning systems
 * some of this class is auto-generated by the associated python scripts
 */
class Quantizer
{
  public:

    Quantizer();
    Quantizer(int scale);
    QuantizeResponse Quantize(int in);
    void SetScale(int scale);
    float GetValueForNote(int note);

    // Bank and scale stuff
    Quantizer(int bank, int scale);
    void SetScale(int bank, int scale);

  protected:

    static const int PROGMEM bankandscale[6][12]; // index from bank-and-scale to scale

    // INSERT AUTOGENERATED SCALE HEADER DATA HERE
#if SCALESET == 0
const static int scaleCount = 68;
static const int *hints[68];
static const float *scales[68];
static const int notecount[68];

static const float PROGMEM scale0[61];
static const int PROGMEM hints0[61];
static const float PROGMEM scale1[36];
static const int PROGMEM hints1[36];
static const float PROGMEM scale2[36];
static const int PROGMEM hints2[36];
static const float PROGMEM scale3[36];
static const int PROGMEM hints3[36];
static const float PROGMEM scale4[26];
static const int PROGMEM hints4[26];
static const float PROGMEM scale5[26];
static const int PROGMEM hints5[26];
static const float PROGMEM scale6[31];
static const int PROGMEM hints6[31];
static const float PROGMEM scale7[31];
static const int PROGMEM hints7[31];
static const float PROGMEM scale8[16];
static const int PROGMEM hints8[16];
static const float PROGMEM scale9[16];
static const int PROGMEM hints9[16];
static const float PROGMEM scale10[21];
static const int PROGMEM hints10[21];
static const float PROGMEM scale11[21];
static const int PROGMEM hints11[21];
static const float PROGMEM scale12[36];
static const int PROGMEM hints12[36];
static const float PROGMEM scale13[37];
static const int PROGMEM hints13[37];
static const float PROGMEM scale14[36];
static const int PROGMEM hints14[36];
static const float PROGMEM scale15[37];
static const int PROGMEM hints15[37];
static const float PROGMEM scale16[36];
static const int PROGMEM hints16[36];
static const float PROGMEM scale17[37];
static const int PROGMEM hints17[37];
static const float PROGMEM scale18[36];
static const int PROGMEM hints18[36];
static const float PROGMEM scale19[36];
static const int PROGMEM hints19[36];
static const float PROGMEM scale20[37];
static const int PROGMEM hints20[37];
static const float PROGMEM scale21[36];
static const int PROGMEM hints21[36];
static const float PROGMEM scale22[37];
static const int PROGMEM hints22[37];
static const float PROGMEM scale23[36];
static const int PROGMEM hints23[36];
static const float PROGMEM scale24[37];
static const int PROGMEM hints24[37];
static const float PROGMEM scale25[37];
static const int PROGMEM hints25[37];
static const float PROGMEM scale26[36];
static const int PROGMEM hints26[36];
static const float PROGMEM scale27[36];
static const int PROGMEM hints27[36];
static const float PROGMEM scale28[37];
static const int PROGMEM hints28[37];
static const float PROGMEM scale29[36];
static const int PROGMEM hints29[36];
static const float PROGMEM scale30[37];
static const int PROGMEM hints30[37];
static const float PROGMEM scale31[36];
static const int PROGMEM hints31[36];
static const float PROGMEM scale32[36];
static const int PROGMEM hints32[36];
static const float PROGMEM scale33[37];
static const int PROGMEM hints33[37];
static const float PROGMEM scale34[36];
static const int PROGMEM hints34[36];
static const float PROGMEM scale35[36];
static const int PROGMEM hints35[36];
static const float PROGMEM scale36[37];
static const int PROGMEM hints36[37];
static const float PROGMEM scale37[36];
static const int PROGMEM hints37[36];
static const float PROGMEM scale38[37];
static const int PROGMEM hints38[37];
static const float PROGMEM scale39[36];
static const int PROGMEM hints39[36];
static const float PROGMEM scale40[37];
static const int PROGMEM hints40[37];
static const float PROGMEM scale41[36];
static const int PROGMEM hints41[36];
static const float PROGMEM scale42[37];
static const int PROGMEM hints42[37];
static const float PROGMEM scale43[36];
static const int PROGMEM hints43[36];
static const float PROGMEM scale44[36];
static const int PROGMEM hints44[36];
static const float PROGMEM scale45[37];
static const int PROGMEM hints45[37];
static const float PROGMEM scale46[27];
static const int PROGMEM hints46[27];
static const float PROGMEM scale47[27];
static const int PROGMEM hints47[27];
static const float PROGMEM scale48[26];
static const int PROGMEM hints48[26];
static const float PROGMEM scale49[27];
static const int PROGMEM hints49[27];
static const float PROGMEM scale50[26];
static const int PROGMEM hints50[26];
static const float PROGMEM scale51[27];
static const int PROGMEM hints51[27];
static const float PROGMEM scale52[27];
static const int PROGMEM hints52[27];
static const float PROGMEM scale53[26];
static const int PROGMEM hints53[26];
static const float PROGMEM scale54[27];
static const int PROGMEM hints54[27];
static const float PROGMEM scale55[26];
static const int PROGMEM hints55[26];
static const float PROGMEM scale56[27];
static const int PROGMEM hints56[27];
static const float PROGMEM scale57[32];
static const int PROGMEM hints57[32];
static const float PROGMEM scale58[31];
static const int PROGMEM hints58[31];
static const float PROGMEM scale59[32];
static const int PROGMEM hints59[32];
static const float PROGMEM scale60[32];
static const int PROGMEM hints60[32];
static const float PROGMEM scale61[31];
static const int PROGMEM hints61[31];
static const float PROGMEM scale62[31];
static const int PROGMEM hints62[31];
static const float PROGMEM scale63[31];
static const int PROGMEM hints63[31];
static const float PROGMEM scale64[32];
static const int PROGMEM hints64[32];
static const float PROGMEM scale65[31];
static const int PROGMEM hints65[31];
static const float PROGMEM scale66[32];
static const int PROGMEM hints66[32];
static const float PROGMEM scale67[32];
static const int PROGMEM hints67[32];
#else
const static int scaleCount = 66;
static const int *hints[66];
static const float *scales[66];
static const int notecount[66];

static const float PROGMEM scale0[61];
static const int PROGMEM hints0[61];
static const float PROGMEM scale1[36];
static const int PROGMEM hints1[36];
static const float PROGMEM scale2[61];
static const int PROGMEM hints2[61];
static const float PROGMEM scale3[36];
static const int PROGMEM hints3[36];
static const float PROGMEM scale4[66];
static const int PROGMEM hints4[66];
static const float PROGMEM scale5[216];
static const int PROGMEM hints5[216];
static const float PROGMEM scale6[26];
static const int PROGMEM hints6[26];
static const float PROGMEM scale7[36];
static const int PROGMEM hints7[36];
static const float PROGMEM scale8[61];
static const int PROGMEM hints8[61];
static const float PROGMEM scale9[86];
static const int PROGMEM hints9[86];
static const float PROGMEM scale10[26];
static const int PROGMEM hints10[26];
static const float PROGMEM scale11[36];
static const int PROGMEM hints11[36];
static const float PROGMEM scale12[61];
static const int PROGMEM hints12[61];
static const float PROGMEM scale13[96];
static const int PROGMEM hints13[96];
static const float PROGMEM scale14[156];
static const int PROGMEM hints14[156];
static const float PROGMEM scale15[26];
static const int PROGMEM hints15[26];
static const float PROGMEM scale16[36];
static const int PROGMEM hints16[36];
static const float PROGMEM scale17[61];
static const int PROGMEM hints17[61];
static const float PROGMEM scale18[96];
static const int PROGMEM hints18[96];
static const float PROGMEM scale19[26];
static const int PROGMEM hints19[26];
static const float PROGMEM scale20[36];
static const int PROGMEM hints20[36];
static const float PROGMEM scale21[61];
static const int PROGMEM hints21[61];
static const float PROGMEM scale22[61];
static const int PROGMEM hints22[61];
static const float PROGMEM scale23[61];
static const int PROGMEM hints23[61];
static const float PROGMEM scale24[61];
static const int PROGMEM hints24[61];
static const float PROGMEM scale25[61];
static const int PROGMEM hints25[61];
static const float PROGMEM scale26[61];
static const int PROGMEM hints26[61];
static const float PROGMEM scale27[61];
static const int PROGMEM hints27[61];
static const float PROGMEM scale28[61];
static const int PROGMEM hints28[61];
static const float PROGMEM scale29[61];
static const int PROGMEM hints29[61];
static const float PROGMEM scale30[61];
static const int PROGMEM hints30[61];
static const float PROGMEM scale31[61];
static const int PROGMEM hints31[61];
static const float PROGMEM scale32[61];
static const int PROGMEM hints32[61];
static const float PROGMEM scale33[61];
static const int PROGMEM hints33[61];
static const float PROGMEM scale34[6];
static const int PROGMEM hints34[6];
static const float PROGMEM scale35[11];
static const int PROGMEM hints35[11];
static const float PROGMEM scale36[16];
static const int PROGMEM hints36[16];
static const float PROGMEM scale37[21];
static const int PROGMEM hints37[21];
static const float PROGMEM scale38[26];
static const int PROGMEM hints38[26];
static const float PROGMEM scale39[31];
static const int PROGMEM hints39[31];
static const float PROGMEM scale40[36];
static const int PROGMEM hints40[36];
static const float PROGMEM scale41[41];
static const int PROGMEM hints41[41];
static const float PROGMEM scale42[46];
static const int PROGMEM hints42[46];
static const float PROGMEM scale43[51];
static const int PROGMEM hints43[51];
static const float PROGMEM scale44[56];
static const int PROGMEM hints44[56];
static const float PROGMEM scale45[66];
static const int PROGMEM hints45[66];
static const float PROGMEM scale46[71];
static const int PROGMEM hints46[71];
static const float PROGMEM scale47[76];
static const int PROGMEM hints47[76];
static const float PROGMEM scale48[81];
static const int PROGMEM hints48[81];
static const float PROGMEM scale49[86];
static const int PROGMEM hints49[86];
static const float PROGMEM scale50[91];
static const int PROGMEM hints50[91];
static const float PROGMEM scale51[96];
static const int PROGMEM hints51[96];
static const float PROGMEM scale52[101];
static const int PROGMEM hints52[101];
static const float PROGMEM scale53[106];
static const int PROGMEM hints53[106];
static const float PROGMEM scale54[111];
static const int PROGMEM hints54[111];
static const float PROGMEM scale55[116];
static const int PROGMEM hints55[116];
static const float PROGMEM scale56[121];
static const int PROGMEM hints56[121];
static const float PROGMEM scale57[36];
static const int PROGMEM hints57[36];
static const float PROGMEM scale58[36];
static const int PROGMEM hints58[36];
static const float PROGMEM scale59[36];
static const int PROGMEM hints59[36];
static const float PROGMEM scale60[26];
static const int PROGMEM hints60[26];
static const float PROGMEM scale61[26];
static const int PROGMEM hints61[26];
static const float PROGMEM scale62[31];
static const int PROGMEM hints62[31];
static const float PROGMEM scale63[16];
static const int PROGMEM hints63[16];
static const float PROGMEM scale64[16];
static const int PROGMEM hints64[16];
static const float PROGMEM scale65[21];
static const int PROGMEM hints65[21];
#endif
    // END AUTOGENERATED SCALE HEADER DATA
      
  private:
    
    int _scale;
    int _octave;
    int _index;
    int _nudge;
    int _above;
    int _below;
    int _current;
    QuantizeResponse _last;

    int _temp;

};

#endif

