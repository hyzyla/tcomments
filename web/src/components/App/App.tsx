import React from 'react';
import css from './App.module.css';
import { Post } from "../Post/Post";
import { Comments } from "../Comments/Comments";

export const App = () => {
    const post = {
        title: 'HTML елемент <section>',
        text: "являє собою узагальнену секцію документу, яка допомагає категоризувати контент, зазвичай, заголовком. Кожний елемент <section> повинен бути ідентифікований, зазвичай, використанням заголовків (<h1>-<h6> element) в якості дочірнього елементу <section>.",
        date: '1.01.2012',
    };
    const author1 = {
        id: '1',
        name: 'Name1',
    };
    const author2 = {
        id: '2',
        name: 'Name2',
    };
    const comments = [
        {
            id: '1',
            text: 'Comment 1',
            author: author1,
            date: '1.01.2012',
            children: [
                {
                    id: '3',
                    text: 'Comment 3',
                    author: author2,
                    date: '1.01.2012',
                    children: [
                        {
                            id: '7',
                            text: 'Comment 7',
                            author: author2,
                            date: '1.01.2012',
                        },
                    ]
                },
                {
                    id: '4',
                    text: 'Comment 4',
                    author: author2,
                    date: '1.01.2012',
                },
                {
                    id: '5',
                    text: 'Comment 5',
                    author: author2,
                    date: '1.01.2012',
                },
            ],
        },
        {
            id: '2',
            text: 'Comment 2',
            author: author2,
            date: '1.01.2012',
        },
    ];
    return (
        <div className={css.root}>
            <div className={css.article}>
                <Post post={post}/>
                <Comments comments={comments}/>
            </div>
        </div>
    );
};
