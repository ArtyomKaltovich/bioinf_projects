- download data
- install callisto


    $ pip install kb-python
    
- build index


    $ kb ref -i transcriptome.idx -g transcripts_to_genes.txt -f1 cdna.fa ref.gz genes.gff.gz
    [2020-04-15 16:43:51,838]   ERROR An exception occurred
    Traceback (most recent call last):
      File "/home/my/.local/lib/python3.8/site-packages/kb_python/main.py", line 483, in main
        COMMAND_TO_FUNCTION[args.command](args)
      File "/home/my/.local/lib/python3.8/site-packages/kb_python/main.py", line 103, in parse_ref
        ref(
      File "/home/my/.local/lib/python3.8/site-packages/kb_python/ref.py", line 272, in ref
        t2g_result = create_t2g_from_gtf(gtf_path, t2g_path)
      File "/home/my/.local/lib/python3.8/site-packages/kb_python/ref.py", line 104, in create_t2g_from_gtf
        transcript_id = entry['group']['transcript_id']
    KeyError: 'transcript_id'
    
- probably kb doesn't support gff, download gffread for converting


    $ ~/bin/gffread-0.11.8.Linux_x86_64/gffread genes.gff.gz -T -o genes.gtf
    Warning: invalid start coordinate at line:
    ��I�i�a��;�j%�x�ozi�<�X|�.!�>\�4��7�j���������e%5e      U
                                                             74:�4N�r���i�U�� ��Q�pF�:�z��H�3�Ωr��
                                                                                                  �_8��┬�����≠�┤��/����⎻�JH�8���─䔄$I���$$�W≥��B���ݜ� └J    �Q      Z�'�H␌$Q���Ԅ#D%ܐL�����±��┼±-2��?���␉�T�,�힓^└   ���V└   ��┴�    ޓJ����E^N�      ┬HL����A�≤��␉┬┬-(F���d�&d�Ħ/������c�%&�o���o���+t:oo!�Y�kP��~+�jJ(��UŘ������k9�']1��\ވ��54�

- unpacking gz archive to genes.gff
    
    
    $ ~/bin/gffread-0.11.8.Linux_x86_64/gffread genes.gff -T -o genes.gtf
    
- build index


    $ kb ref -i transcriptome.idx -g transcripts_to_genes.txt -f1 cdna.fa ref.gz genes.gtf
    
- count


    $ kb count -i transcriptome.idx -g transcripts_to_genes.txt -x 10xv2 --h5ad --loom -t 4 fermentation_0_replicate_1.fastq.gz fermentation_0_replicate_2.fastq.gz -o fermentation_0
    $ kb count -i transcriptome.idx -g transcripts_to_genes.txt -x 10xv2 --h5ad --loom -t 4 fermentation_30_replicate_1.fastq.gz fermentation_30_replicate_2.fastq.gz -o fermentation_30
    