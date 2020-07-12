import React, { FC } from 'react'

import { Post } from '../../types'

import css from './PostCard.module.css';

interface Props {
    post: Post;
}

export const PostCard: FC<Props> = ({ post }) => {
    return (
        <div className={css.card}>
            {post.text}
        </div>
    )
};
