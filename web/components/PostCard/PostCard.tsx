import React, { FC } from 'react'

import { Post } from '../../types'

import css from './PostCard.module.css';

interface Props {
    post: Post;
}

export const PostCard: FC<Props> = ({ post }) => {
    return (
        <div className={css.card}>
            {post.text.split('\n').map((line, idx) => {
                return <p key={idx} className={css.paragraph}>{line}</p>;
            })}
        </div>
    )
};
