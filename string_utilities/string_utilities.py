def string_aggregator(l: list, sep="") -> str:
  return sep.join(l)

def get_string_separators_changed(s, old_sep=" ", new_sep="-"):
    return string_aggregator(s.split(old_sep), new_sep)


if __name__ == "__main__":
    print(get_string_separators_changed("TIH-536 Change Transformation code for TARIFF_FILING_DATA to populate mng_ppl_id and dataset_list_id from the Source_file table"))
    print(get_string_separators_changed("TIH-538 Change Transformation code for TRNS_FIRM to populate mng_ppl_id and dataset_list_id from the Source_file table"))