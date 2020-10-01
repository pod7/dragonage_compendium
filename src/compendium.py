import pandas as pd
from typing import Union
import re

from .util import dialogue_text, codex_text


class DragonAgeCompendium:

    def __init__(self):

        # TODO: use os
        self.cdf = pd.read_csv('../../data/origins/csv/cleaned/t_codex_clean.csv')
        self.ddf = pd.read_csv('../../data/origins/csv/cleaned/t_dialogue_clean.csv')
        self.jdf = pd.read_csv('../../data/origins/csv/cleaned/t_all.csv')

        self.c_mids = []
        self.d_mids = []

        self.as_txt = False
        self.save_results = False
        self.search_term = ""

    def search(self, search_term: str, resource_type: str) -> Union[None, pd.DataFrame]:

        if not isinstance(search_term, str):
            # TODO: RaiseError
            print("Search term must be a string.Please choose one of the following:\n")
            print("'dialogue'\n'codex'\n'both'")
            return

        if resource_type == 'dialogue':
            result = self.search_dialogue(search_term)

        elif resource_type == 'codex':
            result = self.search_codex(search_term)

        elif resource_type == 'both':
            result = self.search_all(search_term)

        else:
            # TODO: Raise error
            print("Incorrect resource type selected; please choose one of the following:\n")
            print("'dialogue'\n'codex'\n'both'")

        return result

    def search_dialogue(self, search_term: str) -> Union[None, pd.DataFrame]:
        '''
        Searches all lines of dialogue for <search_term>

        Parameters:
        -----------
        search_term: str
            keyword to search for

        Returns:
        --------
        if `as_txt` is set to `True`, then results are written to a txt file

        if `as_txt` is set to `False` (the default), then results are saved as
        a csv file and a pd.Dataframe object is returned
        '''
        df = self.ddf

        df = df.loc[df['Text'].str.contains(search_term, flags=re.IGNORECASE)]

        if self.save_results:
            if self.as_txt:
                txt = dialogue_text(df, search_term)
                return txt
            else:
                df.to_csv('results_{}.csv'.format(search_term))
                return df
        else:
            return df

    def search_codex(self, search_term: str) -> Union[None, pd.DataFrame]:
        '''
        Searches all codex entries for <search_term>

        Parameters:
        -----------
        search_term: str
            keyword to search for

        Returns:
        --------
        if `as_txt` is set to `True`, then results are written to a txt file

        if `as_txt` is set to `False` (the default), then results are saved as
        a csv file and a pd.Dataframe object is returned
        '''

        df = self.cdf
        mask = df['Summary'].str.contains(search_term, flags=re.IGNORECASE) | df['Contents'].str.contains(search_term, flags=re.IGNORECASE)
        df = df.loc[mask]

        if self.save_results:
            if self.as_txt:
                txt = codex_text(df, search_term)
                return txt
            else:
                df.to_csv('results_{}.csv'.format(search_term))
                return df
        else:
            return df

    def search_all(self, search_term):
        '''
        Searches all lines of dialogue and all codex entries for <search_term>

        Parameters:
        -----------
        search_term: str
            keyword to search for

        Returns:
        --------
        Results are saved as a csv file and a pd.Dataframe object is returned

        # TODO: add option to return raw text file
        '''
        cdf = self.search_codex(search_term)
        ddf = self.search_dialogue(search_term)

        jdf = ddf.merge(cdf, on=['ModuleResRefVersionID', 'StringID'], how='left')
        jdf = jdf.sort_values(['ModuleResRefVersionID', 'StringID'])

        if self.save_results:
            jdf.to_csv('results_{}.csv'.format(search_term))
        else:
            return jdf

    def npc(self, name: str) -> Union[None, pd.DataFrame]:
        '''
        Looks up all dialogue lines spoken by <name>

        Parameters:
        -----------
        name: str
            Case-sensitive

        Returns:
        --------
        if `as_txt` is set to `True`, then results are written to a txt file

        if `as_txt` is set to `False` (the default), then results are saved as
        a csv file and a pd.Dataframe object is returned
        '''

        df = self.ddf.loc[self.ddf['Speaker'] == '{}'.format(name)]

        if self.as_txt:
            txt = dialogue_text(df, name)
            print(f"Saved as {name}_dlg.txt")
        else:
            df = df[['Speaker', 'VoiceOverComment', 'Text']]
            df.to_csv('{}_dlg.csv'.format(name))
            print(f"Saved as {name}_dlg.csv")
            return df

    def conversations(self, name):
        # returns conversations between anyone and "name"
        pass






